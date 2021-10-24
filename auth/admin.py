from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

from auth.models import Skill, Social, User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
    )

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "about")}),
        (
            _("Permissions"),
            {
                "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions"),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    fields = ("name", "logo", "link")
    list_display = ("name", "link")
    search_fields = ("name",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    fields = ("name", "logo", "description")
    list_display = ("name", "description")
    search_fields = ("name",)
