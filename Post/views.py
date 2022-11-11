from rest_framework import permissions,viewsets
from .serializers import PostSerializer,CategorySerializer
from .models import Post,Category
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-id")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(["GET"])
# @permission_classes([permissions.IsAuthenticated])
def PostCategory(request,pk):
    posts = Post.objects.filter(category=pk).order_by("post_date")
    serializer = PostSerializer(posts,many=True)
    return Response(serializer.data)

