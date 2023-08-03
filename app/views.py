from django.shortcuts import render
from .models import User, Post


def users(request):
	users = User.objects.all()
	context = {
		'users': users,
	}
	return render(request, 'users.html', context)

def user_posts(request, user_id):
	user_posts = Post.objects.filter(user=user_id)
	context = {
		'user_posts': user_posts,
	}
	return render(request, 'user_posts.html', context)

def add_post(request):
	if request.method == 'POST':
		pass 
	return render(request, 'add_post.html')


def register(request):
	return render(request, 'registration/register.html')

def login(request):
	return render(request, 'registration/login.html')