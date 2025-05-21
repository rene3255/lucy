import os
import django
from decouple import config
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from lucy_core import routing
from . import urls


setting_module = config("DJANGO_SETTINGS_MODULE")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{setting_module}")


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns)),
    }
)
