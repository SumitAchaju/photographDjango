from django.urls import path
from Follow.views import UserFriend,FriendPosts
from Account.views import RegisterView
from Post.views import PostCategory,SinglePost,AddComment


urlpatterns = [
    path("friend/",UserFriend),
    path("friendposts/",FriendPosts),
    path("register/",RegisterView.as_view()),
    path("categoryposts/<pk>",PostCategory),
    path("singlepost/<pk>",SinglePost),
    path("addcomment/<pk>",AddComment),
]