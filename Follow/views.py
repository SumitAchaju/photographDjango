from rest_framework import viewsets,permissions
from Follow.models import Friend
from Follow.serializers import AllFriend
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from Post.serializers import PostSerializer
from Post.models import Post

class AllFriendsViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all().order_by('-id')
    serializer_class = AllFriend
    permission_classes = [permissions.IsAuthenticated]



@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def UserFriend(request):
    friends = Friend.objects.filter(user=request.user.id).order_by("-id")
    serializer = AllFriend(friends,many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def FriendPosts(request):
    friends = Friend.objects.filter(user=request.user.id).order_by("-id")
    friend_id = []
    for friend in friends:
        friend_id.append(friend.friends.id)
    friend_posts = Post.objects.filter(user__in=list(friend_id)).order_by("post_date")
    serializer = PostSerializer(friend_posts,many=True)
    return Response(serializer.data)

