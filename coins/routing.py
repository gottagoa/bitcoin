# # crypto_platform/crypto_platform/routing.py

# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from django.urls import path
# from .consumers import CryptoPriceConsumer

# application = ProtocolTypeRouter({
#     'websocket': URLRouter(
#        [
#             path("ws/bitcoin", CryptoPriceConsumer.as_asgi()),
#        ]
#     ),
# })


from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, re_path
from django.core.asgi import get_asgi_application
from .consumers import CryptoPriceConsumer  # Adjust this import based on your actual project structure
from . import consumers
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        [
            re_path(r"ws/bitcoin/", CryptoPriceConsumer.as_asgi()),
        ]
    ),
})

# websocket_urlpatterns =[
#     re_path(r"ws/bitcoin", consumers.CryptoPriceConsumer.as_asgi())
# ]

# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import path
# from .consumers import CryptoPriceConsumer

# websocket_urlpatterns = [
#     path('ws/bitcoin/', CryptoPriceConsumer.as_asgi()),
# ]