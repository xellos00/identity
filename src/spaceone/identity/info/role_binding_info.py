import functools
from spaceone.api.identity.v1 import role_binding_pb2
from spaceone.core.pygrpc.message_type import *
from spaceone.core import utils
from spaceone.identity.model.role_binding_model import RoleBinding
from spaceone.identity.info.role_info import RoleInfo
from spaceone.identity.info.project_info import ProjectInfo
from spaceone.identity.info.project_group_info import ProjectGroupInfo

__all__ = ['RoleBindingInfo', 'RoleBindingsInfo']


def RoleBindingInfo(role_binding_vo: RoleBinding, minimal=False):
    info = {
        'role_binding_id': role_binding_vo.role_binding_id,
        'resource_type': role_binding_vo.resource_type,
        'resource_id': role_binding_vo.resource_id,
        'role_info': RoleInfo(role_binding_vo.role, minimal=True) if role_binding_vo.role else None
    }

    if not minimal:
        info.update({
            'project_info': ProjectInfo(role_binding_vo.project, minimal=True) if role_binding_vo.project else None,
            'project_group_info': ProjectGroupInfo(role_binding_vo.project_group, minimal=True) if role_binding_vo.project_group else None,
            'labels': change_list_value_type(role_binding_vo.labels),
            'tags': change_struct_type(utils.tags_to_dict(role_binding_vo.tags)),
            'domain_id': role_binding_vo.domain_id,
            'created_at': utils.datetime_to_iso8601(role_binding_vo.created_at)
        })

        if not role_binding_vo.project_id and role_binding_vo.project:
            role_binding_vo.update({'project_id': role_binding_vo.project.project_id})

        if not role_binding_vo.project_group_id and role_binding_vo.project_group:
            role_binding_vo.update({'project_group_id': role_binding_vo.project_group.project_group_id})

    return role_binding_pb2.RoleBindingInfo(**info)


def RoleBindingsInfo(role_binding_vos, total_count, **kwargs):
    results = list(map(functools.partial(RoleBindingInfo, **kwargs), role_binding_vos))

    return role_binding_pb2.RoleBindingsInfo(results=results, total_count=total_count)
