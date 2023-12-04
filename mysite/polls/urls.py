from django.urls import path

from . import views

# 命名空间方法2 app_name = 'polls'
urlpatterns = [
    path('index', views.entry_list, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('', views.set_cookie, name='set_cookie'),
]
