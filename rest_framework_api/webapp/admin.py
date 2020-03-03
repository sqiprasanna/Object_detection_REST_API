from django.contrib import admin
# from webapp.models import Employees
# Register your models here.
# admin.site.register(Employees)
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from webapp.models import *

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "first_name", "last_name", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = ((None,{"classes": ("wide",),"fields": ("email","first_name","last_name","password1","password2",),},),)
    list_display = (
        "email",
        "first_name",
        "last_name",
    )
    search_fields = (
        "email",
        "first_name",
        "last_name",
    )
    ordering = ("-id",)

    ordering = ("-id",)

