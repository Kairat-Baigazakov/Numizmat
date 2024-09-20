# Тут мы импортируем views, для дальнейшей работы с html
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('info', views.info, name='info'),
    path('coin/<int:pk>/', views.coin_detail, name='coin_detail'),
    path('coin/add/', views.coin_add, name='coin_add'),
    path('coin/<int:pk>/edit/', views.coin_edit, name='coin_edit'),
    path('loginuser/', views.login_user, name='login_user'),
]
