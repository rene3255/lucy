from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumerGeneral(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "lucyschat"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        await self.accept()

        await self.send(
            json.dumps(
                {
                    "type": "connection_established",
                    "message": "Connected to global chat!",
                }
            )
        )

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message = data.get("message", "").strip()
            if not message:
                return
        except json.JSONDecodeError:
            await self.send(json.dumps({"error": "Paquete de datos inválido"}))
            return
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
            },
        )

    async def chat_message(self, event):
        await self.send(
            json.dumps(
                {
                    "type": "chat",
                    "message": event["message"],
                }
            )
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Access the user from self.scope
        user = self.scope.get("user", None)
        if not user or user.is_anonymous:
            print("Anonymous user - denaying connection")
            await self.close()
            return

        print("USUARIO AUTHENTICATED:", user.id)

        self.room_group_name = f"user_{user.id}"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        await self.accept()

        await self.send(
            text_data=json.dumps(
                {
                    "type": "connection_established",
                    "message": "You are now connected",
                }
            )
        )

    async def disconnect(self, close_code):
        if hasattr(self, "room_group_name"):
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name,
            )

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)

        except json.JSONDecoderError:
            await self.send(text_data=json.dumps({"error": "Invalid JSON format"}))
            return
        message = text_data_json.get("message", "")
        action = text_data_json.get("action")

        if action == "ping":
            await self.send(text_data=json.dumps({"type": "chat", "message": "pong"}))
            return

        if isinstance(message, str):
            try:
                message = json.loads(message)
            except json.JSONDecodeError:
                message = {"action": "text", "content": message}

        if message:

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": (
                        message
                        if isinstance(message, dict)
                        else {"action": "text", "content": str(message)}
                    ),
                },
            )

    async def chat_message(self, event):
        message = event["message"]
        if isinstance(message, dict) and message.get("action") == "text":
            content = message.get("content", "")

            await self.send(
                text_data=json.dumps(
                    {
                        "type": "chat",
                        "message": content,
                    }
                )
            )
        else:
            await self.send(
                text_data=json.dumps(
                    {
                        "type": "chat",
                        "message": message,
                    }
                )
            )

    async def send_notification(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "type": "notification",
                    "message": event["message"],
                }
            )
        )


from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.sessions.models import Session
import json


class ChatConsumerWithSessions(AsyncWebsocketConsumer):
    async def connect(self):
        # Get user and session from the connection scope
        user = self.scope.get("user")
        session = self.scope.get("session")

        # Handle anonymous users with sessions
        if not user or user.is_anonymous:
            # Create a session if it doesn't exist
            if not session or not session.session_key:
                session = self.scope["session"]
                await database_sync_to_async(session.create)()  # Create session in DB
                await database_sync_to_async(session.save)()

            self.room_group_name = f"anon_{session.session_key}"
            user_type = "anonymous"
        else:
            # Authenticated user
            self.room_group_name = f"user_{user.id}"
            user_type = "authenticated"

        # Join the group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

        # Send connection confirmation
        await self.send(
            json.dumps(
                {
                    "type": "connection_established",
                    "message": "Connection successful",
                    "user_type": user_type,
                    "group": self.room_group_name,
                }
            )
        )

    async def disconnect(self, close_code):
        # Leave the group
        if hasattr(self, "room_group_name"):
            await self.channel_layer.group_discard(
                self.room_group_name, self.channel_name
            )

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message = data.get("message")
        except json.JSONDecodeError:
            await self.send(json.dumps({"error": "Invalid JSON"}))
            return

        # Broadcast to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "sender_group": self.room_group_name,
            },
        )

    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(
            json.dumps(
                {
                    "type": "chat",
                    "message": event["message"],
                    "sender_group": event["sender_group"],
                }
            )
        )
