import os
import django
import environ

env = environ.Env()
environ.Env.read_env()
setting_module = env("DJANGO_SETTINGS_MODULE", default="lucy_core.settings.dev")
os.environ["DJANGO_SETTINGS_MODULE"] = setting_module

print("EUREKA", setting_module)

django.setup()


from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from lucy_core import routing
from . import urls

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns)),
    }
)
