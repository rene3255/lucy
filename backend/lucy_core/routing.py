from django.urls import re_path
from applications.lucyschat.consumers import (
    ChatConsumer,
    ChatConsumerWithSessions,
    ChatConsumerGeneral,
)
from decouple import config

# from chat.consumers import ChatConsumer
# from notifications.consumers import NotificationConsumer

if config("AUTH_MIDDLE") == "True":
    websocket_urlpatterns = [
        re_path(r"ws/chat/$", ChatConsumer.as_asgi()),
        # re_path(r"ws/notifications/$", NotificationConsumer.as_asgi()),
    ]
else:
    websocket_urlpatterns = [
        re_path(r"ws/chat/$", ChatConsumerGeneral.as_asgi()),
        # re_path(r"ws/notifications/$", NotificationConsumer.as_asgi()),
    ]
