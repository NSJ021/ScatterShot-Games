# forms.py
from django import forms
from django.contrib.auth.forms import PasswordChangeForm


class UsernameChangeForm(forms.Form):
    new_username = forms.CharField(max_length=150, required=True)


class EmailChangeForm(forms.Form):
    new_email = forms.EmailField(max_length=254, required=True)


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Old Password"
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="New Password"
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm Password"
    )
