from unicodedata import name
from django.urls import path
from . import views

app_name = 'Seller'

urlpatterns = [

    path('add_products',views.add_product,name='add_products'),

]
