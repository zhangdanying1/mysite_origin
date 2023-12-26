from tasks import app
# celery的包下
from celery.result import AsyncResult
# 这里注意改变查找结果的id号
id = '5912561c-c8df-48d3-92cf-248d47b05262'
if __name__ == '__main__':
    a = AsyncResult(id=id, app=app)
    if a.successful():  # 正常执行完成
        result = a.get()  # 任务返回的结果
        print(result)
    elif a.failed():
        print('任务失败')
    elif a.status == 'PENDING':
        print('任务等待中被执行')
    elif a.status == 'RETRY':
        print('任务异常后正在重试')
    elif a.status == 'STARTED':
        print('任务已经开始被执行')