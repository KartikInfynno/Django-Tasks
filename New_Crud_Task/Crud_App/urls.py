from django.urls import path
from . import views

urlpatterns = [
    path('',views.create, name="index"),
    # path('<int:id>/retrive/',views.retrive, name="retrive"),
    path('<int:id>/update/',views.update, name="update"),
    path('<int:id>/delete/',views.delete, name="delete"),

]
