from Follow.models import Friend
from rest_framework import serializers
from Post.serializers import PostSerializer
from Account.serializers import UserSerializer

class AllFriend(serializers.ModelSerializer):
    post= PostSerializer(many=True,read_only=True)
    friends = UserSerializer(read_only=True)
    class Meta:
        model = Friend
        fields = '__all__'
