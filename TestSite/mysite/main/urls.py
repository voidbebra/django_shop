from django.urls import path
from . import views

urlpatterns = [
    path('', views.maine, name='home'),
    path('about-me', views.about, name='about'),
    path('register', views.dj_register, name='register'),
    path('login', views.dj_login, name='login'),
    path('logout', views.dj_logout, name='logout'),
    path('user_list', views.get_user_list, name='user_list'),
    path('products', views.products, name='products'),
    path('products/<int:id>', views.product_detail,
         name='product_detail'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('add/<int:id>/',
         views.cart_add,
         name='cart_add'),
    path('cart/remove/<int:id>/',
         views.cart_remove,
         name='cart_remove'),
]