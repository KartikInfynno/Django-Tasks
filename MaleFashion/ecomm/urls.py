from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index, name='index'),
    path('create', views.add_product, name='create'),
    path('cart', views.cart, name='cart'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('<int:id>/delete_cart/', views.del_item_cart, name='delete_cart'),
    path('<int:id>/delete_wishlist/', views.del_wishlist, name='del_wishlist'),
    path('<int:id>/add_cart',views.add_to_cart, name='add_cart'),
    path('<int:id>/add_wishlist',views.add_wishlist, name='add_wishlist'),
    path('shop', views.shop, name='shop'),

]
