from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	pass

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'telegram_id', 'applications')

class CustomUserChangeForm(UserChangeForm):
	pass

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

