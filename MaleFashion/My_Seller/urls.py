from unicodedata import name
from django.urls import path
from . import views

app_name = 'Seller'

urlpatterns = [

    path('add_products',views.add_product,name='add_products'),

]


#Toster Messages
#Add Filter Approved/Not Approved
#Search Title
#Category And Tags Filter Frontend
#Comment Approved by Blog Poster
#Fav Blog
#Blog View Counter
#Multiple Image Slider
#related Product user specified/sys specified
#Author Details Most Popular Post Of THat User
#Socia Media Sharing with desc img title ,fb,twitter
