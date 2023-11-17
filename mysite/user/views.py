from django.shortcuts import render, redirect
from django.shortcuts import reverse
from .form import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# 使用表单实现用户注册
def registerView(request):
    if request.method == 'POST':
        user = MyUserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            tips = '注册成功'
            messages.success(request, '注册完了马上来登录吧！')
            return redirect(reverse('user:login'))
        else:
            tips = '注册失败'
    user = MyUserCreationForm()
    return render(request, 'user/user.html', locals())


# 用户登录
def loginView(request):
    tips = '请登录, 才能投票'
    userLogin = True
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
    return render(request, 'user/user.html', locals())


# 退出登录
def logoutView(request):
    logout(request)
    return redirect(reverse('user:login'))
