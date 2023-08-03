from django import forms
from .models import User


class RegisterForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={
		'name': 'name',
		'placeholder': 'Имя',
		'required': '',
	}))
	email = forms.EmailField(widget=forms.TextInput(attrs={
		'name': 'email',
		'placeholder': 'E-mail',
		'required': '',
	}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={
		'name': 'password',
		'placeholder': 'Пароль',
		'required': '',
	}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		'name': 'password2',
		'placeholder': 'Подтвердить пароль',
		'required': '',
	}))

	def clean_name(self):
		name = self.cleaned_data['name']
		user = User.objects.filter(name=name)
		if user.exists():
			raise forms.ValidationError('Такое имя уже занято')
		return name
	def clean_email(self):
		email = self.cleaned_data['email']
		user = User.objects.filter(email=email)
		if user.exists():
			raise forms.ValidationError('Такой E-mail уже занят')
		return email

	def clean_password2(self):
		password = self.cleaned_data['password']
		password2 = self.cleaned_data['password2']
		if password2 != password:
			raise forms.ValidationError('Пароли не совпадают')

class LoginForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={
		'name': 'name',
		'placeholder': 'Имя',
		'required': '',
	}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={
		'name': 'password',
		'placeholder': 'Пароль',
		'required': '',
	}))
