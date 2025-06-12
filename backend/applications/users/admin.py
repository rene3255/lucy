from django.contrib import admin
from applications.users.models.users import User
from applications.users.models.user_profile import UserProfile


admin.site.register(User)
