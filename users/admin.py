from django.contrib.auth.admin import UserAdmin
from users.forms import LoginForm, ProfileForm
from django.contrib import admin
from users.models import User


class CustomUserAdmin(UserAdmin):
    add_form = LoginForm
    form = ProfileForm
    model = User

    list_display = ("id", "email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    list_display_links = ("email",)

    fieldsets = (('Main', {"fields": ("email", "password",)}),
                 ('Access rights', {"fields": ("is_staff", "is_active",
                                    "groups", "user_permissions")}
                 ),
                )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2",
                "is_staff", "is_active", "groups", "user_permissions",
            )
        }
        ),
    )
    
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)
