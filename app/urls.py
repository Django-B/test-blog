from django.urls import path
from . import views

urlpatterns = [
	path('users/', views.users, name='users'),
	path('users/<int:user_id>/posts/', views.user_posts, name='user_posts'),

	path('add_post/', views.add_post, name='add_post'),

	path('register/', views.register, name='register'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
]