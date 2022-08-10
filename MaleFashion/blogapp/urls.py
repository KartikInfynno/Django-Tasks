
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog'),
    path('my_blog', views.my_blogs, name='my_blog'),
    path('<int:id>/blog_details', views.blog_details, name='blog_detail'),
    path('<int:id>/blog_delete', views.blog_delete, name='blog_delete'),
    path('<int:id>/add_fav_blog', views.add_fav_blog, name='add_fav_blog'),
    path('<int:id>/remove_fav', views.rem_fav_blog, name='rem_fav_blog'),
    path('blog_post', views.blog_create, name='blog_post'),
    path('fav_blogs', views.fav_blogs, name='fav_blog'),
    path('admin_approval', views.admin_approval, name='admin_approve'),
    path('<int:id>/profile', views.profile_view, name='profile'),
]
