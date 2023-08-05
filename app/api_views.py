from rest_framework import generics
from .models import User, Post
from .serializers import UserSerializer, PostSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all() # type: ignore 
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all() # type: ignore
    serializer_class = UserSerializer
