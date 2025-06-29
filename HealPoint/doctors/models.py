from django.db.models import (
    CASCADE,
    SET_NULL,
    DateField,
    ForeignKey,
    ImageField,
    OneToOneField,
    TextField
)

from django.utils.translation import gettext_lazy as _

from helpers.model_mixins import BaseMetaMixin, PersonMixin
from stores.models import Store
from users.models import UserHealPoint

class Doctor(PersonMixin):
    user = OneToOneField(
        UserHealPoint, 
        on_delete=CASCADE, 
        related_name="doctor"
    )
    store = ForeignKey(
        Store,
        on_delete=SET_NULL,
        related_name="doctors",
        verbose_name= _("Stores"),
        null=True
    )

    professional_phone = TextField(_("Professional Phone"), max_length=10)

    class Meta:
        verbose_name = _("Doctor")
        verbose_name_plural = _("Doctors")

class ProffesionalLicence(BaseMetaMixin):
    doctor = ForeignKey(Doctor, on_delete=CASCADE, related_name="professional_licenses")
    number = TextField(_("License Number"), max_length=255)
    expiration_date = DateField(_("License Expiration Date"))
    issuing_date = DateField(_("License Issuing Date"))
    image = ImageField(_("License Image"), upload_to="professional_licenses")
    speciality = TextField(_("Speciality"), max_length=255)
    university = TextField(_("University"), max_length=255)

    def __str__(self):
        return f"{self.doctor.full_name} - {self.number}"

    class Meta:
        verbose_name = _("Professional License")
        verbose_name_plural = _("Professional Licenses")
        db_table = "doctors_licenses"