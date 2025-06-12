from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from applications.users.models.users import User
from applications.users.models.user_profile import UserProfile


class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ["email", "username", "is_staff", "is_active"]
    fieldsets = (
        (
            None,
            {"fields": ("email", "first_name", "last_name", "username", "password")},
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )

    def save_model(self, request, obj, form, change):

        if not obj.password.startswith("pbkdf2_"):
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
