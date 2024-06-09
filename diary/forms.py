from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from .models import User, Todo, Page

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

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).exists():
			raise ValidationError("User with this Email address already exists. Or may be the email is not verified yet.")
		return email

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


class TodoForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ('title', 'description')
		widgets = {
			'title': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Write here...'}),
			'description': forms.Textarea(attrs={'class': 'input', 'placeholder': 'Write here...'}),
		}

class PageForm(forms.ModelForm):
	class Meta:
		model = Page
		fields = ('title', 'content')
		widgets = {
			'title': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Write here...'}),
			'content': forms.Textarea(attrs={'class': 'input', 'placeholder': 'Write here...'}),
		}