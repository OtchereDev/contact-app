from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

ROLES = (
    ("Administrator", "Administrator"),
    ("Supervisor", "Supervisor"),
    ("Staff", "Staff"),
)


class User(AbstractUser):
    role = models.CharField(_("Your Role"), max_length=15, choices=ROLES)
