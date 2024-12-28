from django.contrib import admin
from accounts.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ("id","username","password", "email")

admin.site.register(User, UserAdmin)
