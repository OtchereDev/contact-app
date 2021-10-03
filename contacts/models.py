from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contact(models.Model):
    name = models.CharField(_("Your Full Name"), max_length=255)
    email = models.EmailField(_("Your Email"), max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name + " " + self.email
