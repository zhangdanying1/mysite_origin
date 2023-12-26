from django.db import models


class BaseModel(models.Model):
    """
        公共字段创建基表 ---- 其他表也可能用
        id img图片地址 上传时间 是否删除 是否显示 显示排序
    """
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    is_show = models.BooleanField(default=True, verbose_name='是否上架')
    orders = models.IntegerField(verbose_name='优先级')

    class Meta:
        abstract = True  # 不迁移生成表

