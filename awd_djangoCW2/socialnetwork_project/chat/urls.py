from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='chat-home'),
    path('<str:room_name>/', views.room, name='room'),
]