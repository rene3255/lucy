from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from applications.users.models.users import User
from applications.users.models.user_profile import UserProfile


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display = [
        "email",
        "first_name",
        "last_name",
        "username",
        "role",
        "is_staff",
        "is_active",
    ]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "username", "role")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Important Dates",
            {"fields": ("date_joined",)},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "username",
                    "role",
                    "password",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

    def save_model(self, request, obj, form, change):

        if not obj.password.startswith("pbkdf2_"):
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(UserProfile)
