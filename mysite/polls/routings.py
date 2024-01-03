from django.urls import path
from . import consumers

# 这个变量是存放websocket的路由
websocket_urlpatterns = [
    path('polls/socket', consumers.ChatConsumer.as_asgi()),
]
