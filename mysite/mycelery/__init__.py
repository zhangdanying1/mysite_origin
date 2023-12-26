from __future__ import absolute_import
from celery import Celery
from django.conf import settings
import os

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('tasks')
app.config_from_object('mycelery.tasks.config')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
