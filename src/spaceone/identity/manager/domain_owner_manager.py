import re
import logging

from spaceone.core.manager import BaseManager
from spaceone.identity.lib.cipher import PasswordCipher
from spaceone.identity.model.domain_owner_model import DomainOwner
from spaceone.identity.error.error_user import *

_LOGGER = logging.getLogger(__name__)


class DomainOwnerManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.domain_owner_model: DomainOwner = self.locator.get_model('DomainOwner')

    def create_owner(self, params):
        def _rollback(vo):
            _LOGGER.info(f'[create_owner._rollback] Delete domain owner : {vo["owner_id"]} ({vo["domain_id"]})')
            vo.delete()

        if params.get('password'):
            self._check_password_format(params['password'])
            hashed_pw = PasswordCipher().hashpw(params['password'])
            params['password'] = hashed_pw

        domain_owner: DomainOwner = self.domain_owner_model.create(params)

        self.transaction.add_rollback(_rollback, domain_owner)

        return domain_owner

    def update_owner(self, params):
        def _rollback(old_vo):
            _LOGGER.info(f'[update_owner._rollback] Revert domain owner : {old_vo["name"]} ({old_vo["domain_id"]})')
            domain_owner.update(old_vo)

        if params.get('password'):
            self._check_password_format(params['password'])
            hashed_pw = PasswordCipher().hashpw(params['password'])
            params['password'] = hashed_pw

        domain_owner: DomainOwner = self.domain_owner_model.get(owner_id=params['owner_id'], domain_id=params['domain_id'])

        self.transaction.add_rollback(_rollback, domain_owner.to_dict())

        return domain_owner.update(params)

    def delete_owner(self, domain_id, owner_id):
        domain_owner: DomainOwner = self.domain_owner_model.get(domain_id=domain_id, owner_id=owner_id)
        domain_owner.delete()

    def get_owner(self, domain_id, owner_id=None, only=None):
        if owner_id:
            return self.domain_owner_model.get(domain_id=domain_id, owner_id=owner_id, only=only)
        else:
            return self.domain_owner_model.get(domain_id=domain_id, only=only)

    @staticmethod
    def _check_password_format(password):
        if len(password) < 8:
            raise ERROR_INCORRECT_PASSWORD_FORMAT(rule='At least 9 characters long.')
        elif not re.search("[a-z]", password):
            raise ERROR_INCORRECT_PASSWORD_FORMAT(rule='Contains at least one lowercase character')
        elif not re.search("[A-Z]", password):
            raise ERROR_INCORRECT_PASSWORD_FORMAT(rule='Contains at least one uppercase character')
        elif not re.search("[0-9]", password):
            raise ERROR_INCORRECT_PASSWORD_FORMAT(rule='Contains at least one number')
