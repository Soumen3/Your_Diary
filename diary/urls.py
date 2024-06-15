from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	# -------------------User Authentication------------------- #
	path("accounts/login/", views.user_login, name="login"),
	path("accounts/logout/", views.user_logout, name="logout"),
	path("accounts/signup/", views.user_signup, name="signup"),

	# -------------------Extra------------------- #
	path("", views.home, name="home"),
	path("about/", views.about, name="about"),
	path('profile/', views.profile, name="profile"),
	path('profile/update/', views.update_profile, name="updateProfile"),
	path('profile/delete/', views.delete_profile, name="deleteProfile"),

	# -------------------My Diary------------------- #
	path("my-diary/", views.myDairy, name="myDiary"),
	path("my-diary/write-page/", views.writePage, name="writePage"),
	path("my-diary/update-page/<int:id>/", views.updatePage, name="updatePage"),
	path("my-diary/view-page/<int:id>/", views.viewPage, name="viewPage"),
	path("my-diary/delete-page/<int:id>/", views.deletePage, name="deletePage"),

	# -------------------Todo------------------- #
	path("todo/", views.todo, name="todo"),
	path("todo/add-todo", views.addTodo, name="addTodo"),
	path("todo/update-todo/<int:id>/", views.updateTodo, name="updateTodo"),
	path("todo/delete-todo/<int:id>/", views.deleteTodo, name="deleteTodo"),

	# -------------------Password Reset------------------- #
	path("reset_password/", auth_views.PasswordResetView.as_view(template_name = "password-reset/reset_password.html"), name="reset_password"),
	path("reset_password_done/", auth_views.PasswordResetDoneView.as_view(template_name = "password-reset/reset_password_done.html"), name="password_reset_done"),
	path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name = "password-reset/reset_password_confirm.html"), name="password_reset_confirm"),
	path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name = "password-reset/reset_password_complete.html"), name="password_reset_complete"),

	# -------------------Password Change------------------- #
	path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password-change/password_change.html'), name='password_change'),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password-change/password_change_done.html'), name='password_change_done'),

	# -------------------Email Verification------------------- #
	path('verification/', include('verify_email.urls')),
	path('verificatoin-msg/', views.verifiacation, name="verificationMsg"),
]
