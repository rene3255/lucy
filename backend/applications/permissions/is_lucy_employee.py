from rest_framework.permissions import BasePermission
from applications.reference_data.enums.user_role import UserRole

"""
SUPER_ADMIN = "superadmin", "Super Admin"
ADMIN = "administrador", "Administrador"
MODERATOR = "moderador", "Moderador"
REGULAR_USER = "usuario_regular", "Usuario regular"

"""


class IsLucyEmployee(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        return (
            request.user.is_superuser
            or request.user.is_staff
            or request.user.is_active
            or request.user.role
            in [
                UserRole.SUPER_ADMIN,
                UserRole.ADMIN,
                UserRole.MODERATOR,
                UserRole.REGULAR_USER,
            ]
        )
