from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    UserSearch,
    listusers,
    change_friends,
    ProfileView
   
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='social-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('search/', views.UserSearch, name='profile-search'),
    path('userprofile/<int:pk>', ProfileView.as_view(), name='user-profile'),
    path('friend/', views.listusers, name='listusers'),
    path('friend/<str:operation>/<int:pk>/', views.change_friends, name='change_friends'),
]