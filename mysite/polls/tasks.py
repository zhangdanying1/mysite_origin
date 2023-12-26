import datetime
from time import sleep
from celery import shared_task
import logging
logger = logging.getLogger(__name__)


@shared_task()
def task1(x):
    for i in range(int(x)):
        sleep(1)
        logger.info('this is task1 '+str(i))
    return x


@shared_task
def scheduletask1():
    now = datetime.datetime.now()
    logger.info('this is scheduletask '+now.strftime("%Y-%m-%d %H:%M:%S"))
    return None
