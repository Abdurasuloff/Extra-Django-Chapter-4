from channels.generic.websocket import AsyncWebsocketConsumer
import json


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "notification_room"
        
        #Userni guruhga qo'shish
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()
        
        
        #Test sifatida Notification yuborish
        await self.channel_layer.group_send(
            self.room_name,
            {"message":"Channels bilan Notification", "type":"send_notification"}
        )
        
        
    async def disconnect(self, close_code):
        # Userni guruhdan chiqarib yuborish
        await self.channel_layer.group_discard(self.room_name, self.channel_name)
    
    
    async def recieve(self):
        pass
    
    async def send_notification(self, event):
        message = event['message']
        
        await self.send(text_data=json.dumps({"message":message}))