from django.urls import path

from . import views

urlpatterns = [
    path('<int:book_id>/', views.product_display, name='display'),
]
