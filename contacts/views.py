from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from decorators.decorators import administrator_user

from contacts.forms import ContactForm
from .models import Contact


class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, "add.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "success.html")
        return render(request, "add.html", {"form": form})


@method_decorator(login_required, name="dispatch")
@method_decorator(administrator_user, name="dispatch")
class ContactListView(View):
    def get(self, request, *args, **kwargs):
        contacts = Contact.objects.all()
        return render(request, "contact-list.html", {"contacts": contacts})
