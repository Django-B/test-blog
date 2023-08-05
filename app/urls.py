from django.urls import path
from . import views
from .api_views import UserRetrieveUpdateDestroyView, UserListCreateView

urlpatterns = [
	path('users/', views.users, name='users'),
	path('users/<int:user_id>/posts/', views.user_posts, name='user_posts'),

	path('add_post/', views.add_post, name='add_post'),
	path('delete_post/', views.delete_post, name='delete_post'),

	path('register/', views.register, name='register'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),

    # DRF API
    path('api/users/', UserListCreateView.as_view(), name='user-list'),
    path('api/users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
]
