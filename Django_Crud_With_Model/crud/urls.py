from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('create/',views.create,name="create"),
    path('<int:id>/detail/',views.retrive,name="detail"),
    path('<int:id>/update/',views.update,name="update"),
    path('<int:id>/delete/',views.delete,name="delete"),


]
