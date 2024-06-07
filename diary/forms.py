from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
	date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class':'input', 'range': '1900-01-01, 2021-12-31'}))
	email = forms.EmailField(label="Email address", 
						  widget=forms.EmailInput(attrs={'class': 'input' , 'placeholder':'Write here...'}))
	first_name = forms.CharField(label="First name",
						  widget=forms.TextInput(attrs={'class': 'input' ,'placeholder':'Write here...'}))
	last_name = forms.CharField(label="Last name",
						  widget=forms.TextInput(attrs={'class': 'input' ,'placeholder':'Write here...'}))
	password1 = forms.CharField(label="Password",
						  widget=forms.PasswordInput(attrs={'class': 'input' ,'placeholder':'Write here...'}))	
	password2 = forms.CharField(label="Password confirmation",
						  widget=forms.PasswordInput(attrs={'class': 'input' ,'placeholder':'Write here...'}))
	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name', 'date_of_birth')

class CustomUserChangeForm(UserChangeForm):
	date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'range': '1900-01-01, 2021-12-31'}))
	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name', 'date_of_birth')

class LoginForm(forms.Form):
	email = forms.EmailField(label="Email address", widget=forms.EmailInput(attrs={'class': 'form-control' , 'id':'floatingInput', 'placeholder':'Email'}))
	password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'id':'floatingPassword', 'placeholder':'Password'}))
	
	def __init__(self, *args, **kwargs):
		kwargs.setdefault('label_suffix', '')
		super(LoginForm, self).__init__(*args, **kwargs)