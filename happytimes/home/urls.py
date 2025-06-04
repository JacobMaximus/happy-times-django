from django.urls import path
from . import views
from .views import signup_view, login_view, user_login_page, profile_view, logout_view

urlpatterns = [
    path('home', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('cart/', views.cart, name='cart'),
    # path('login/', views.login, name='login'),
    # path('admin-login/', views.admin, name='admin'),
    # path('admin-panel/', views.admin_panel, name='admin-panel'),
    # path('user-login', views.user_login, name='user-login'),

    path('api/signup/', signup_view, name='signup'),
    path('api/login/', login_view, name='login'),
    path('', views.home, name='home'),
    path('login/', user_login_page, name='login_page'),

    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),

]