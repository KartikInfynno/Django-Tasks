from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_system, name = 'login'),
    path('profile/', views.profile_page, name = 'profile')
]
