from django.db import models


class User(models.Model):
	name = models.CharField(max_length=100, unique=True)
	email = models.EmailField()
	password = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	body = models.TextField()

	def __str__(self):
		return self.title
