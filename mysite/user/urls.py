from django.urls import path
from .views import *

urlpatterns = [
    path('', registerView, name='register'),
]
