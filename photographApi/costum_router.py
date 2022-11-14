from django.urls import path
from Follow.views import UserFriend,FriendPosts
from Account.views import RegisterView
from Post.views import PostCategory,SinglePost,AddComment,DeleteComment,PostLikes,PostLikesOut


urlpatterns = [
    path("friend/",UserFriend),
    path("friendposts/",FriendPosts),
    path("register/",RegisterView.as_view()),
    path("categoryposts/<pk>",PostCategory),
    path("singlepost/<pk>",SinglePost),
    path("addcomment/<pk>",AddComment),
    path("deletecomment/<pk>",DeleteComment),
    path("postlike/<pk>",PostLikes),
    path("postlikeout/<pk>",PostLikesOut),
]