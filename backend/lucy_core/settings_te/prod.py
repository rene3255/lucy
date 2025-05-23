from .base import *
import dj_database_url
import environ

env = environ.Env()
environ.Env.read_env()

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": ["redis://:lucychat1234@137.184.49.56:6379/0"],
            "channel_capacity": {
                "http.request": 1000,
                "http.response!*": 1000,
                "websocket.send": 1000,
            },
        },
    },
}
WEBSOCKET_TIMEOUT = 180
ASGI_THREADS = 4
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
