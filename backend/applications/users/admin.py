from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from applications.users.models.users import User
from applications.users.models.user_profile import UserProfile


class CustomUserAdmin(admin.ModelAdmin):
    model = User
    list_display = [
        "email",
        "first_name",
        "last_name",
        "username",
        "is_staff",
        "is_active",
    ]
    fields = ["email", "first_name", "last_name", "password"]

    def save_model(self, request, obj, form, change):

        if not obj.password.startswith("pbkdf2_"):
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
