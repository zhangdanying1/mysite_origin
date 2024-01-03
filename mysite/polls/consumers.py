from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from django.core import serializers
from django.conf import settings
from django.utils import timezone
from .models import Banner
import time


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        print("正在连接")
        # 发起请求之后自动创建连接
        # 客户端与服务端进行握手时，会触发这个方法
        # 服务端允许客户端进行连接，就是握手成功
        self.accept()

    def websocket_receive(self, content, **kwargs):
        print("服务端接收到客户端消息: ", content)

        cnt = 1
        while True:
            now = timezone.now()
            banner_list_query = Banner.objects.all().filter(show_time__lte=now).filter(end_show_time__gte=now).order_by(
                '-orders')[:settings.BANNER_COUNT]
            banner_list = serializers.serialize("json", banner_list_query)
            print("banner_list: ", banner_list)

            time.sleep(1)
            cnt += 1
            if cnt <= (settings.WS_SEND_FREQUENCY if settings.WS_SEND_FREQUENCY else 10):
                self.send(banner_list)   # 每秒服务端向client发送一次数据数据，持续时间 WS_SEND_FREQUENCY or 10s
            else:
                break

    def disconnect(self, close_code):
        print('客户端断开连接')
        raise StopConsumer(close_code)
