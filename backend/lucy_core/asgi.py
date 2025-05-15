import os
from decouple import config
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lucy_core.settings.prod"),
django_application = get_asgi_application()
auth_middle = config("AUTH_MIDDLE")
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack

from .routing import websocket_urlpatterns
from . import urls

if auth_middle == "True":  # When the Django environment uses Auth (JWT or AuthO2)

    application = ProtocolTypeRouter(
        {
            "http": get_asgi_application(),
            "websocket": AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
        }
    )
else:

    application = ProtocolTypeRouter(
        {
            "http": get_asgi_application(),
            "websocket": SessionMiddlewareStack(URLRouter(websocket_urlpatterns)),
        }
    )
