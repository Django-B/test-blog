from django.shortcuts import render


def users(request):
	return render(request, 'users.html')

def user_posts(request, user_id):
	return render(request, 'user_posts.html')

def add_post(request):
	if request.method == 'POST':
		pass 
	return render(request, 'add_post.html')

def register(request):
	return render(request, 'registration/register.html')

def login(request):
	return render(request, 'registration/login.html')