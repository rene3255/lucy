from django.db import models


class UserRole(models.TextChoices):
    SUPER_ADMIN = "superadmin", "Super Admin"
    ADMIN = "administrador", "Administrador"
    MODERATOR = "moderador", "Moderador"
    REGULAR_USER = "usuario_regular", "Usuario regular"
