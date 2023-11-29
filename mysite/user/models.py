from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    qq = models.CharField('QQ号码', max_length=16, blank=True, null=True)
    weChat = models.CharField('微信账号', max_length=100, blank=True, null=True)
    mobile = models.CharField('手机号码', max_length=11, blank=True, null=True)
    # blank=True, null=True代表可以不填写，不填写的时候设置为空值

    # 设置返回值
    def __str__(self):
        return self.username
