from django.shortcuts import render, redirect
from django.shortcuts import reverse
from .form import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


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
        if MyUser.objects.filter(username=u):
            user = authenticate(username=u, password=p)
            if user:
                if user.is_active:
                    # 登录当前用户
                    login(request, user)
                return redirect(reverse('polls:index'))
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
        form = MyPasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)   # dont logout the user.
            messages.success(request, "Password changed.")
            return redirect(reverse('polls:index'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "user/change_password.html", {'form': form})
