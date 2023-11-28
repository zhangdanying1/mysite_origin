from django.urls import path
from .views import *

urlpatterns = [
    path('', register, name='register'),
    path('login.html', login, name='login'),
    path('logout.html', logout, name='logout'),
]

