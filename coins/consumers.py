# crypto_platform/crypto_prices/consumers.py

import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import CryptoPrice
from .serializers import CryptoPriceSerializer
from asgiref.sync import sync_to_async

class CryptoPriceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            "type": "connection_established",
            "message": "You are connected"
        }))
        asyncio.create_task(self.send_data_periodically())

    
    @sync_to_async
    def get_all_crypto_prices(self):
        return list(CryptoPrice.objects.all())

    async def send_data_periodically(self):
        while True:
            crypto_prices = await self.get_all_crypto_prices()
            serializer = CryptoPriceSerializer(instance=crypto_prices, many=True)
            data = serializer.data

            await self.send(json.dumps(data))
            await asyncio.sleep(3)

    async def disconnect(self, close_code):
        if hasattr(self, 'send_data_task'):
            self.send_data_task.cancel()
    
