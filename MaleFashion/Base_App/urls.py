from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/product_detail/',views.product_details,name='product_detail'),
    path('cart',views.cart,name='cart'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('<int:id>/add_cart',views.add_cart,name='add_cart'),
    path('<int:id>/add_wishlist',views.add_wishlist,name='add_wishlist'),
    path('<int:id>/remove_cart',views.del_cart,name='remove_cart'),
    path('<int:id>/remove_wishlist',views.del_wishlist,name='remove_wishlist'),
    path('shop',views.shop,name='shop'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('test',views.test,name='test'),
]
