from django.shortcuts import render, redirect
from .forms import LoginForm, CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def user_login(request):
	context = {}
	if request.method == "POST":
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			email = login_form.cleaned_data["email"]
			password = login_form.cleaned_data["password"]
			user = authenticate(request, email=email, password=password)
			if user is not None:
				login(request, user)
				# Redirect to the home page
				return redirect("home")
			else:
				context["login_form"] = login_form
				messages.error(request, "Invalid email or password")
				# Display an error message and the login form

			
			# Authenticate the user
			# If the user is authenticated, redirect to the home page
			# If the user is not authenticated, display an error message
			# and the login form
	else:
		login_form = LoginForm()
		context["login_form"] = login_form
	return render(request, "login.html", context)

def user_logout(request):
	logout(request)
	return redirect("login")


def home (request):
	return render(request, "home.html")