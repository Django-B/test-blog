from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password


class User(models.Model):
	name = models.CharField(max_length=100, unique=True)
	email = models.EmailField()
	password = models.CharField(max_length=100)

	def check_pass(self, password):
		 return check_password(password, self.password)


	def save(self, *args, **kwargs):
	    # Хэшируем пароль перед сохранением объекта
	    self.password = make_password(self.password)
	    super().save(*args, **kwargs)
	    
	def __str__(self):
		return self.name

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	body = models.TextField()


	def __str__(self):
		return self.title
