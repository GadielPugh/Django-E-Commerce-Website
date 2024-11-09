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
        fields = ['address', 'bank_account_name', 'bank_account_number']
        labels = {
            'address': 'Physical Address',
            'bank_account_name': 'Bank Account Name',
            'bank_account_number': 'Bank Account Number'
        }