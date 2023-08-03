from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .models import User, Post
from .forms import RegisterForm, LoginForm


def users(request):
	users = User.objects.all()
	context = {
		'users': users,
	}
	return render(request, 'users.html', context)

def user_posts(request, user_id):
	user = User.objects.get(pk=user_id)
	user_posts = Post.objects.filter(user=user_id)
	context = {
		'post_user': user,
		'user_posts': user_posts,
	}
	return render(request, 'user_posts.html', context)

def add_post(request):
	if request.method == 'POST':
		pass 
	return render(request, 'add_post.html')


def register(request):
	form = RegisterForm()
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			new_user = authenticate(request, name=name, email=email, password=password)
			# new_user = add_user(name, email, password)

			return redirect('login')

	context = {
		'form': form
	}

	return render(request, 'registration/register.html', context)

def login(request):
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			password = form.cleaned_data['password']

			# Проверка данных на корректность
			user = User.objects.filter(name=name)
			if not user.exists() or not user.first().check_pass(password):
				form.add_error('password', 'Неправильное имя или пароль')

			request.session['user_id'] = user.first().pk
			return redirect('users')
			
	context = {
		'form': form
	}

	return render(request, 'registration/login.html', context)

def logout(request):
	if request.method == 'POST':
		url_name = request.POST['url_name']
		request.session['user_id'] = ''
		return redirect(url_name)


def add_user(name, email, password):
	new_user = User(name=name, email=email, password=password)
	new_user.save()
	return new_user