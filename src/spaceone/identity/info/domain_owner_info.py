from spaceone.api.identity.v1 import domain_owner_pb2

from spaceone.core import utils
from spaceone.identity.model import DomainOwner

__all__ = ['DomainOwnerInfo']


def DomainOwnerInfo(owner_vo: DomainOwner, minimal=False):
    info = {
        'owner_id': owner_vo.owner_id,
        'name': owner_vo.name
    }

    if not minimal:
        info.update({
            'email': owner_vo.email,
            'language': owner_vo.language,
            'timezone': owner_vo.timezone,
            'domain_id': owner_vo.domain_id,
            'last_accessed_at': utils.datetime_to_iso8601(owner_vo.last_accessed_at),
            'created_at': utils.datetime_to_iso8601(owner_vo.created_at)

        })

    return domain_owner_pb2.DomainOwnerInfo(**info)
