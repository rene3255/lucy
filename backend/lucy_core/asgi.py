import os
from decouple import config
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lucy_core.settings.prod")
django_application = get_asgi_application()

auth_middle = config("AUTH_MIDDLE", default="True")
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack

from .routing import websocket_urlpatterns
from . import urls

middleware_stack = (
    AuthMiddlewareStack if auth_middle == "True" else SessionMiddlewareStack
)
# When the Django environment uses Auth (JWT or AuthO2)

application = ProtocolTypeRouter(
    {
        "http": django_application,
        "websocket": middleware_stack(URLRouter(websocket_urlpatterns)),
    }
)
