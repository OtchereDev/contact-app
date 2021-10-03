from django.forms import ModelForm
from django import forms
from .models import Contact


class ContactForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'block py-2 px-2 w-full rounded-md mb-3 outline-none', 'autoComplete': "off"}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'block py-2 px-2 w-full rounded-md outline-none', "autoComplete": "off", "type": "email"}))

    class Meta:
        model = Contact
        fields = "__all__"
