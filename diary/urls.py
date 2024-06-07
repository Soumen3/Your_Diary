from django.urls import path
from . import views

urlpatterns = [
	path("login/", views.user_login, name="login"),
	path("logout/", views.user_logout, name="logout"),
	path("signup/", views.user_signup, name="signup"),
	path("", views.home, name="home"),
	path("about/", views.about, name="about"),
	path("my-diary/", views.myDairy, name="myDiary"),
	path("todo/", views.todo, name="todo"),
	path("todo/add-todo", views.addTodo, name="addTodo"),
	path("todo/update-todo/<int:id>/", views.updateTodo, name="updateTodo"),
	path("todo/delete-todo/<int:id>/", views.deleteTodo, name="deleteTodo"),
]
