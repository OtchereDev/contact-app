from django.urls import path
from .views import ContactListView, ContactView


urlpatterns = [
    path("contacts/", ContactListView.as_view()),
    path("", ContactView.as_view()),
]
