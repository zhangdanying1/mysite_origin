from django.shortcuts import render, redirect
from django.shortcuts import reverse
from .form import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import QueryDict


# 使用表单实现用户注册
def register(request):
    if request.method == 'POST':
        user = MyUserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect(reverse('user:login'))
    else:
        user = MyUserCreationForm()
    return render(request, 'user/user.html', {'user': user})


# 用户登录
def login_re(request):
    tips = '请登录'
    user_login = True
    if request.method == 'POST':
        u = request.POST.get('username', '')
        p = request.POST.get('password1', '')

        # 摘取验证码表单
        query_dict = QueryDict(mutable=True)
        query_dict['captcha_1'] = request.POST.get('captcha_1')
        query_dict['captcha_0'] = request.POST.get('captcha_0')
        captcha_form = CaptchaForm(query_dict)

        if MyUser.objects.filter(username=u):
            user = authenticate(username=u, password=p)
            if user:
                if user.is_active:
                    if captcha_form.is_valid():
                        # 登录当前用户
                        login(request, user)
                        return redirect(reverse('polls:index'))
                    else:
                        tips = "验证码错误，请重新输入"
                else:
                    tips = '账号失效，请联系管理员'
            else:
                tips = '账号密码错误，请重新输入'
        else:
            tips = '用户不存在，请注册'
    user = MyUserCreationForm()
    return render(request, 'user/user.html', {'tips': tips, 'user_login':  user_login, 'user': user})


# 退出登录
def logout_re(request):
    logout(request)
    return redirect(reverse('user:login'))


@login_required(login_url='/login.html')
def change_ps(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)   # dont logout the user.
            messages.success(request, "Password changed.")
            return redirect(reverse('polls:index'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "user/change_password.html", {'form': form})


def find_ps(request):
    if request.POST:
        form = MyPasswordResetForm(request.POST)
        if form.is_valid():
            try:
                form.save(domain_override=request.get_host(),
                          email_template_name="user/password_reset_email.txt",
                          from_email=settings.EMAIL_HOST_USER, request=request)
                messages.success(request, '重设密码的链接已经发送到您的邮箱')
            except Exception as e:
                print(e)
                messages.error(request, "Email sending failed. Please try again.")
            return redirect(reverse('user:login'))
    else:
        form = MyPasswordResetForm()
    return render(request, "user/find_password.html", {'form': form})
