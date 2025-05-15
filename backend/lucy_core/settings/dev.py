from .base import *
from decouple import config


DEBUG = config("DEBUG", default=False, cast=bool)
print("DEBUG EN DEV", DEBUG)
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
print("ALLOWED_HOSTS =", ALLOWED_HOSTS)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}
