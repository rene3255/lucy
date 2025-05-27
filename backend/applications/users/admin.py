from django.contrib import admin
from applications.users.models.users import User
from applications.users.models.user_profile import UserProfile

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
