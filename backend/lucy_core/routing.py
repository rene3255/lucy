from django.urls import re_path

# from chat.consumers import ChatConsumer
# from notifications.consumers import NotificationConsumer

websocket_urlpatterns = [
    # re_path(r"ws/chat/$", ChatConsumer.as_asgi()),
    # re_path(r"ws/notifications/$", NotificationConsumer.as_asgi()),
]
