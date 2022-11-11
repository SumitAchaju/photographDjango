from django.urls import path
from Follow.views import UserFriend,FriendPosts
from Account.views import RegisterView
from Post.views import PostCategory


urlpatterns = [
    path("friend/",UserFriend),
    path("friendposts/",FriendPosts),
    path("register/",RegisterView.as_view()),
    path("categoryposts/<pk>",PostCategory),
]