from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.login, name='login'),
    path('admin-login/', views.admin, name='admin'),
    path('admin-panel/', views.admin_panel, name='admin-panel'),
]