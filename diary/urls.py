from django.urls import path
from . import views

urlpatterns = [
	path("login/", views.user_login, name="login"),
	path("logout/", views.user_logout, name="logout"),
	path("signup/", views.user_signup, name="signup"),
	path("", views.home, name="home"),
	path("about/", views.about, name="about"),
	path("my-diary/", views.myDairy, name="myDiary"),
	path("plans/", views.plans, name="plans")
]
