from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog'),
    path('my_blog', views.my_blogs, name='my_blog'),
    path('blog_post', views.blog_create, name='blog_post'),
]
