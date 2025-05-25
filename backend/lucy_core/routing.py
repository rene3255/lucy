from django.urls import re_path
from applications.lucyschat.consumers import ChatConsumerGeneral
from decouple import config

# from chat.consumers import ChatConsumer
# from notifications.consumers import NotificationConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/$", ChatConsumerGeneral.as_asgi()),
]
