from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('', register, name='register'),
    path('login.html', login_re, name='login'),
    path('logout.html', logout_re, name='logout'),
    path('change_ps.html', change_ps, name='change_password'),
    path('find_ps.html', find_ps, name='find_password'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='user/password_reset_confirm.html',
        success_url=reverse_lazy('user:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='user/password_reset_complete.html'), name='password_reset_complete'),
]
