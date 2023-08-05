from rest_framework import serializers
from .models import User, Post

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

class PostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'
