from django.contrib import admin
from applications.users.models.users import User
from applications.users.models.user_profile import UserProfile


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["email", "username", "is_staff", "is_active"]
    fields = ["email", "username", "password", "is_staff", "is_active"]

    def save_model(self, request, obj, form, change):
        if not change:
            if hasattr(obj, "password") and obj.password:
                if not obj.password.startswith("pbkdf2_"):
                    obj.set_password(obj.password)
        else:
            if "password" in form.changed_data and obj.password:
                if not obj.password.startswith("pbkdf2_"):
                    obj.set_password(obj.password)
        super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
