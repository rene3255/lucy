from .base import *
from decouple import config


DEBUG = config("DEBUG", default=False, cast=bool)
print("DEBUG EN DEV", DEBUG)
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
print("ALLOWED_HOSTS =", ALLOWED_HOSTS)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("DB_NAME_DEV"),
        "USER": config("DB_USER_DEV"),
        "PASSWORD": config("DB_PASSWORD_DEV"),
        "HOST": config("DB_HOST_DEV"),
        "PORT": config("DB_PORT_DEV"),
    }
}
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}
