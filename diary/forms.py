from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name', 'date_of_birth')

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name', 'date_of_birth')

class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)