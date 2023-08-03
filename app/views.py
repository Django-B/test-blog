from django.shortcuts import render, redirect

from .models import User, Post
from .forms import RegisterForm, LoginForm, AddPostForm

from .my_decorators import check_login


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

@check_login
def add_post(request):
	form = AddPostForm()
	if request.method == 'POST':
		form = AddPostForm(request.POST)
		if form.is_valid():
			user_id = request.session.get('user_id')
			user = User.objects.get(pk=user_id)
			title = form.cleaned_data['title']
			body = form.cleaned_data['body']

			post = Post(user=user, title=title, body=body)
			post.save()
			
			return redirect('user_posts', user_id)
		
	context = {
		'form': form
	}
	return render(request, 'add_post.html', context)

@check_login
def delete_post(request):
	if request.method == 'POST':
		user_id = request.session.get('user_id')
		user = User.objects.get(pk=user_id)
		post_id = request.POST['post_id']
		post = Post.objects.get(pk=post_id)
		post.delete()
		
	return redirect('user_posts', user_id)


def register(request):
	form = RegisterForm()
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			new_user = add_user(name, email, password)

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

@check_login
def logout(request):
	print(request.path)
	if request.method == 'POST':
		request.session['user_id'] = ''
		return redirect('users')


def add_user(name, email, password):
	new_user = User(name=name, email=email, password=password)
	new_user.save()
	return new_user

	