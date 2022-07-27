from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.add_data, name='create'),
    path('<int:id>/update', views.update_data, name='update'),
    path('<int:id>/delete', views.delete_data, name='delete'),
]
