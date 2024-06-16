from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Todo, Page, Site, Theme
from .forms import CustomUserCreationForm, CustomUserChangeForm, LoginForm


class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['id', "email", "first_name", "last_name", "date_of_birth", "is_admin", "is_active"]
    list_filter = ["is_admin"]
    list_display_links = ["email"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["first_name", "last_name", "date_of_birth"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "first_name", "last_name", "date_of_birth", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)



@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'description', 'created_at', 'updated_at']
    filter_horizontal = []

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'content', 'created_at', 'updated_at']
    filter_horizontal = []

    class Media:
        js = ('js/tinyInject.js',)  # Specify the path to your JavaScript file



@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'phone', 'facebook', 'twitter', 'instagram']
    filter_horizontal = []



@admin.register(Theme)  # register the model
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'theme', 'change_time']