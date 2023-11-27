"""
ASGI config for bitcoin project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
# import os

# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from bitcoin.coins import routing as coins_routing

# asgi = get_asgi_application()
# os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# application = ProtocolTypeRouter({
#     'http': asgi,
#     'websocket': URLRouter(
#         coins_routing.application()
#     ),
# })


import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from bitcoin.coins import routing

asgi = get_asgi_application()
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

application = ProtocolTypeRouter({
    'http': asgi,
    'websocket': URLRouter(
        routing.application
    ),
})
