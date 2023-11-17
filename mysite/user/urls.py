from django.urls import path
from .views import *

urlpatterns = [
    path('', registerView, name='register'),
    path('login.html', loginView, name='login'),
    path('logout.html', logoutView, name='logout'),
]

