from django.contrib import admin
from .models import User, CustomUserManager
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, UserCreationForm

class UserAdmin(admin.ModelAdmin):
    form = UserCreationForm
    add_form = UserCreationForm
    list_display = ('id', 'email', 'is_staff')
    search_fields = ('email',)

admin.site.register(User, UserAdmin)
