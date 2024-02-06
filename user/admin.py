from django.contrib import admin
from user.models.user import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'is_active')