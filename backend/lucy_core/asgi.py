import os
import django
from decouple import config
from django.core.asgi import get_asgi_application

## setting_module = config("DJANGO_SETTINGS_MODULE")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", default="lucy_core.settings.prod")
django.setup()


auth_middle = config("AUTH_MIDDLE", default="True")
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack

from lucy_core.routing import websocket_urlpatterns
from . import urls

django_application = get_asgi_application()

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
