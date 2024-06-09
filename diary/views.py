from django.shortcuts import render, redirect
from .forms import LoginForm, CustomUserCreationForm, CustomUserChangeForm, TodoForm, PageForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Todo, User, Page
from verify_email.email_handler import send_verification_email

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
				messages.success(request, "You have logged in successfully")
				# Redirect to the home page
				return redirect("home")
			else:
				# login_form = LoginForm()
				# context["login_form"] = login_form
				# Display an error message and the login form
				messages.error(request, "Invalid email or password")

	else:
		login_form = LoginForm()
		
	context["login_form"] = login_form
	return render(request, "login.html", context)

def user_signup(request):
	context = {}
	if request.method == "POST":
		signup_form = CustomUserCreationForm(request.POST)
		if signup_form.is_valid():
			inactive_user = send_verification_email(request, signup_form)
			email = signup_form.cleaned_data.get("email")
			request.session['email'] = email
			messages.success(request, "Verify your email to complete the registration")
			return redirect("verificationMsg")
		else:
			context["signup_form"] = signup_form
			messages.error(request, "Invalid information")

	else:
		signup_form = CustomUserCreationForm()
		context["signup_form"] = signup_form
	return render(request, "signup.html", context)

def user_logout(request):
	logout(request)
	messages.success(request, "You have logged out successfully")
	return redirect("home")

def verifiacation(request):
	context = {}
	email = request.session['email']
	context['email'] = email
	return render(request, "emailVerification/verification_msg.html", context)

def home (request):
	context = {}
	context['activeHome']="active"
	if request.user.is_authenticated:
		context["user"] = request.user
	# 	return render(request, "home.html", context)
	# else:
	# 	return render(request, "home.html")
	return render(request, "home.html", context)

def about(request):
	context = {}
	context['activeAbout']="active"
	return render(request, "about.html", context)


@login_required(login_url="login")
def todo(request):
	context = {}
	todo_form = TodoForm()
	context["todo_form"] = todo_form
	todos = Todo.objects.filter(user=request.user)
	context["todos"] = todos
	context['activeTodo']="active"
	return render(request, "todo.html", context)


@login_required(login_url="login")
def addTodo (request):
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.user = request.user
			todo.save()
			messages.success(request, "You have added a new todo")
			return redirect("todo")
		else:
			messages.error(request, "Error adding a new todo")
			return redirect("todo")
	else:
		form = TodoForm()
		return render(request, "todo.html", {"form": form})

@login_required(login_url="login")
def updateTodo(request, id):
	todo = Todo.objects.get(id=id)
	if request.user != todo.user:
		messages.error(request, "You are not authorized to update this todo")
		return redirect("todo")
	form = TodoForm(instance=todo)
	if request.method == "POST":
		form = TodoForm(request.POST, instance=todo)
		if form.is_valid():
			form.save()
			messages.success(request, "You have updated the todo")
			return redirect("todo")
		else:
			messages.error(request, "Error updating the todo")
			return redirect("todo")
	else:
		return render(request, "updateTodo.html", {"form": form})
	
@login_required(login_url="login")
def deleteTodo(request, id):
	todo = Todo.objects.get(id=id)
	if request.user != todo.user:
		messages.error(request, "You are not authorized to delete this todo")
		return redirect("todo")
	todo.delete()
	messages.success(request, "You have deleted the todo")
	return redirect("todo")



@login_required(login_url="login")
def myDairy(request):
	context = {}
	page_form = PageForm()
	context["page_form"] = page_form
	pages = Page.objects.filter(user=request.user).order_by('-created_at')

	context["pages"] = pages
	context['activeDiary']="active"
	return render(request, "myDiary.html", context)

@login_required(login_url="login")
def writePage(request):
	context ={}
	if request.method == "POST":
		page_form = PageForm(request.POST)
		print(request.POST)
		if page_form.is_valid():
			page = page_form.save(commit=False)
			page.user = request.user
			page.save()
			messages.success(request, "You have added a new page")
			return redirect("myDiary")
		else:
			messages.error(request, "Error adding a new page")
			return redirect("myDiary")
	else:
		page_form = PageForm()
		context["page_form"] = page_form
		return render(request, "writePage.html", {"page_form": page_form})

@login_required(login_url="login")
def updatePage(request, id):
	context={}
	page = Page.objects.get(id=id)
	if request.user != page.user:
		messages.error(request, "You are not authorized to update this page")
		return redirect("myDiary")
	form = PageForm(instance=page)
	if request.method == "POST":
		form = PageForm(request.POST, instance=page)
		if form.is_valid():
			form.save()
			messages.success(request, "You have updated the page")
			return redirect("myDiary")
		else:
			messages.error(request, "Error updating the page")
			return redirect("myDiary")
	else:
		context["page_form"] = form
		return render(request, "writePage.html", context)

login_required(login_url="login")
def viewPage(request, id):
	context = {}
	page = Page.objects.get(id=id)
	if request.user != page.user:
		messages.error(request, "You are not authorized to view this page")
		return redirect("myDiary")
	context["page"] = page
	return render(request, "viewPage.html", context)

@login_required(login_url="login")
def deletePage(request, id):
	page = Page.objects.get(id=id)
	if request.user != page.user:
		messages.error(request, "You are not authorized to delete this page")
		return redirect("myDiary")
	page.delete()
	messages.success(request, "You have deleted the page")
	return redirect("myDiary")