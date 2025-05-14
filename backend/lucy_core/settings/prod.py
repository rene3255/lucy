from .base import *
import dj_database_url
from decouple import config

DEBUG = config("DEBUG", default=False, cast=bool)
print("EN PROD ", DEBUG)
ALLOWED_HOSTS = config("ALLOWED_HOSTS").split(",")
DATABASES = {
    "default": dj_database_url.parse(config("DATABASE_URL")),
}

SECURE_HSTS_SECONDS = 3600
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
