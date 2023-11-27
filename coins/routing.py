
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, re_path
from django.core.asgi import get_asgi_application
from .consumers import CryptoPriceConsumer


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        [
            re_path(r"ws/bitcoin/", CryptoPriceConsumer.as_asgi()),
        ]
    ),
})

