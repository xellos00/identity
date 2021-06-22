import functools
from spaceone.core.pygrpc.message_type import *
from spaceone.api.identity.v1 import user_pb2

__all__ = ['FindUserInfo', 'FindUsersInfo']


def FindUserInfo(user_data: dict, minimal=False):
    info = {
        'user_id': user_data.get('user_id'),
        'name': user_data.get('name'),
        'email': user_data.get('email')
    }
    if not minimal:
        tags = {}
        for tag in user_data.get('tags', []):
            tags[tag['key']] = tag['value']

        info.update({
            'tags': change_struct_type(tags),
        })

    return user_pb2.FindUserInfo(**info)


def FindUsersInfo(find_users_vos, total_count, **kwargs):
    results = list(map(functools.partial(FindUserInfo, **kwargs), find_users_vos))
    return user_pb2.FindUsersInfo(results=results, total_count=total_count)
