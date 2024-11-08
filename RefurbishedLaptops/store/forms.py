from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    address = forms.CharField(max_length=255, required=True)
    bank_details = forms.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'address', 'bank_details')