from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from applications.users.managers import UserManager
from applications.reference_data.enums.user_role import UserRole


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=20, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    role = models.CharField(
        max_length=30, choices=UserRole.choices, null=True, blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]

    class Meta:
        db_table = "users"

    def __str__(self):
        return str(self.username)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = User.objects.generate_unique_username(
                self.first_name, self.last_name
            )
        super().save(*args, **kwargs)
