import datetime
from time import sleep
from celery import shared_task
import logging
logger = logging.getLogger(__name__)



# @shared_task
# def change_pic():
#     from .models import Banner
#     from django.conf import settings
#     banner_list = Banner.objects.all().filter(is_delete=False, is_show=True).order_by('orders')[:settings.BANNER_COUNT]
#     return banner_list
#
#
# @shared_task
# def change_pic_back():
#     from .models import Banner
#     from django.conf import settings
#     banner_list = Banner.objects.all().filter(is_delete=False, is_show=True).order_by('-orders')[:settings.BANNER_COUNT]
#     return banner_list
