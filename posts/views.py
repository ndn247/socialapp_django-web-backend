from models import Post, TestModel
from posts.serializers import PostSerializer, TestModelSerializer, UserSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from posts.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def pre_save(self, obj):
    	obj.owner = self.request.user

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def pre_save(self, obj):
    	obj.owner = self.request.user

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TestModelList(generics.ListCreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer