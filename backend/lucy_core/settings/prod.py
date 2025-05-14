from .base import *
import dj_database_url
from decouple import config

DEBUG = config("DEBUG", default=False, cast=bool)
print("EN PROD ", DEBUG)
ALLOWED_HOSTS = config("ALLOWED_HOSTS").split(",")
DATABASES = {
    "default": dj_database_url.parse(config("DATABASE_URL")),
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(config("REDIS_HOST"), config("REDIS_PORT"))],
        },
    },
}
SECURE_HSTS_SECONDS = 3600
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
