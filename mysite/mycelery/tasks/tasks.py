import time
from .. import app


def send_sms(mobile, code):
    time.sleep(1)
    print('%s手机号，发送短信成功，验证码是：%s' % (mobile, code))
    return True


@app.task
def run():
    send_sms('1822344343', 9999)
    return True


