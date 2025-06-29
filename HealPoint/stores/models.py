from django.db.models import (
    BooleanField,
    TextField,
    URLField,
)

from django.utils.translation import gettext_lazy as _

from helpers.model_mixins import AddressMixin


class Store(AddressMixin):
    name = TextField(_("Name"), max_length=50)
    phone = TextField(_("Phone"), max_length=10, blank=True)
    is_active = BooleanField(_("Is Active"), default=True)

    maps_url = URLField(_("Maps URL "), max_length=350, blank=True)

    class Meta:
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")

    def __str__(self):
        return self.name
