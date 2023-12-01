from django.urls import path
from .views import *

urlpatterns = [
    path('', register, name='register'),
    path('login.html', login_re, name='login'),
    path('logout.html', logout_re, name='logout'),
    path('change_ps.html', change_ps, name='change_password'),
]
