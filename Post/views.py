from rest_framework import permissions,viewsets
from .serializers import PostSerializer,CategorySerializer
from .models import Post,Category,Comment
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from Account.models import User

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-id")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def PostCategory(request,pk):
    if pk == 1:
        posts = Post.objects.all().order_by("post_date")
    else:
        posts = Post.objects.filter(category=pk).order_by("post_date")
    serializer = PostSerializer(posts,many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def SinglePost(request,pk):
    if request.method == "GET":
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post,many=False)
        return Response(serializer.data)

@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def AddComment(request,pk):
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        data = request.data
        user = User.objects.get(id=int(data["userid"]))
        comment = data["comment"]
        new_comment = Comment(comment_by=user,comment=comment)
        new_comment.save()
        post.comment.add(new_comment)
        return Response({"status":"success"})
