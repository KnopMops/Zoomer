from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('meeting/', views.videocall, name="meeting"),
    path('join_room/', views.join_room, name="join_room"),

    path('auth/register/', views.register, name="register"),
    path('auth/login/', views.login, name="login"),
    path('logout/', views.logouta, name="logout"),
]