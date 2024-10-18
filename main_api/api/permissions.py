from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed


class MockedTokenPermission(BasePermission):
    """
    Custom permission to check for a Bearer token in the Authorization header.
    The token will not be validated but must be present.
    """
    def has_permission(self, request, view):
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            raise AuthenticationFailed('Bearer token required')

        return True
