from django.contrib import admin
from applications.users.models.users import User


class CustomUserAdmin(admin.ModelAdmin):
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
