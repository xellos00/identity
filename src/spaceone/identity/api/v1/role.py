from spaceone.api.identity.v1 import role_pb2, role_pb2_grpc
from spaceone.core.pygrpc import BaseAPI


class Role(BaseAPI, role_pb2_grpc.RoleServicer):

    pb2 = role_pb2
    pb2_grpc = role_pb2_grpc

    def create(self, request, context):
        params, metadata = self.parse_request(request, context)

        with self.locator.get_service('RoleService', metadata) as role_svc:
            data = role_svc.create(params)
            return self.locator.get_info('RoleInfo', data)

    def update(self, request, context):
        params, metadata = self.parse_request(request, context)

        with self.locator.get_service('RoleService', metadata) as role_svc:
            data = role_svc.update(params)
            return self.locator.get_info('RoleInfo', data)

    def delete(self, request, context):
        params, metadata = self.parse_request(request, context)

        with self.locator.get_service('RoleService', metadata) as role_svc:
            role_svc.delete(params)
            return self.locator.get_info('EmptyInfo')

    def get(self, request, context):
        params, metadata = self.parse_request(request, context)

        with self.locator.get_service('RoleService', metadata) as role_svc:
            data = role_svc.get(params)
            return self.locator.get_info('RoleInfo', data)

    def list(self, request, context):
        params, metadata = self.parse_request(request, context)

        with self.locator.get_service('RoleService', metadata) as role_svc:
            role_vos, total_count = role_svc.list(params)
            return self.locator.get_info('RolesInfo', role_vos, total_count, minimal=self.get_minimal(params))

    def stat(self, request, context):
        params, metadata = self.parse_request(request, context)

        with self.locator.get_service('RoleService', metadata) as role_svc:
            return self.locator.get_info('StatisticsInfo', role_svc.stat(params))
