from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Transaction

class CustomUserCreationForm(UserCreationForm):
    address = forms.CharField(max_length=255, required=True)
    bank_details = forms.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'address')

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['buyer_name', 'address', 'bank_account_number'] 