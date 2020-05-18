from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('cart/', views.cart, name='cart'),
    path('zahialga/', views.zahialga, name='zahialga'),
    path('login/',views.loginview, name='login'),
    path('cartAdd/',views.cartAdd, name='cartAdd'),
    path('logout/',views.logoutview, name='logout'),
    path('register/',views.register, name='register'),
]
