from __future__ import absolute_import
from celery.schedules import crontab
from datetime import timedelta

# 使用redis存储任务队列
broker_url = 'redis://127.0.0.1:6379/14'
# 使用redis存储结果
result_backend = 'redis://127.0.0.1:6379/15'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
# 时区设置
timezone = 'Asia/Shanghai'
# celery默认开启自己的日志
# False表示不关闭
worker_hijack_root_logger = False
# 存储结果过期时间，过期后自动删除
# 单位为秒
result_expires = 60 * 60 * 24

# 导入任务所在文件
imports = [
    'mycelery.tasks.tasks',
]

# 需要执行任务的配置
beat_schedule = {
    'run_sms': {
        'task': 'mycelery.tasks.tasks.run',
        'schedule': timedelta(seconds=3),
        # 'schedule': crontab(minute="20,21,22", hour=14),
        'args': (),
    },
}
