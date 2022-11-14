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
        post.save()
        return Response(PostSerializer(post).data)


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def DeleteComment(request,pk):
    if request.method == "POST":
        comment = Comment.objects.get(id=pk)
        comment.delete()
        post = Post.objects.get(id=request.data["postid"])
        return Response(PostSerializer(post).data)


@api_view(["GET","POST"])
@permission_classes([permissions.IsAuthenticated])
def PostLikes(request,pk):
    if request.method == "GET":
        post = Post.objects.get(id=pk)
        post.like_by.add(request.user)
        post.save()
        return Response(PostSerializer(post).data)
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        post.like_by.remove(request.user)
        post.save()
        return Response(PostSerializer(post).data)

@api_view(["GET","POST"])
@permission_classes([permissions.IsAuthenticated])
def PostLikesOut(request,pk):
    if request.method == "GET":
        post = Post.objects.get(id=pk)
        post.like_by.add(request.user)
        post.save()
        allpost = Post.objects.all().order_by("post_date")
        return Response(PostSerializer(allpost,many=True).data)
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        post.like_by.remove(request.user)
        post.save()
        allpost = Post.objects.all().order_by("post_date")
        return Response(PostSerializer(allpost,many=True).data)
