from .base import *
import dj_database_url
from decouple import config

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS").split(",")


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
