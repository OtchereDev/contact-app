from django import forms
from .models import User
from django.forms import ModelForm


class UserSignUpForm(ModelForm):
    password = forms.CharField(widget=forms.TextInput(
        attrs={"autoComplete": "off", "type": "password"}))

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "role",
            "password"

        ]
