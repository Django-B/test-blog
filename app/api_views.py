from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Post
from .serializers import UserSerializer, PostSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all() # type: ignore 
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all() # type: ignore
    serializer_class = UserSerializer

class UserPostsAPIView(APIView):
    def get(self, request, user_id):
        posts = Post.objects.filter(user=user_id) # type: ignore
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all() # type: ignore
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all() # type: ignore
    serializer_class = PostSerializer

