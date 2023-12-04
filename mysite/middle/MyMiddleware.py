from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now
from django.shortcuts import Http404


# 给路由设置访问门槛
class MyMiddleware(MiddlewareMixin):
    def process_view(self, request, func, args, kwargs):
        if func.__name__ != 'set_cookie':
            salt = request.COOKIES.get('value', '')
            try:
                request.get_signed_cookie('MySign', salt=salt)
            except Exception as e:
                print(e)
                raise Http404('当前Cookie无效哦！')

    # 响应内容添加Cookie信息, 为下一次请求提供Cookie信息
    def process_response(self, request, response):
        salt = str(now())
        response.set_signed_cookie(
            'MySign',
            'sign',
            salt=salt,
            max_age=3600
        )
        response.set_cookie('value', salt)
        return response
