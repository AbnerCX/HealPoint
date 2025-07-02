from helpers.model_mixins import PersonMixin

from django.db.models import (
    CASCADE,
    SET_NULL,
    BooleanField,
    ForeignKey,

)

from django.utils.translation import gettext_lazy as _

from users.models import UserHealPoint

class Patient(PersonMixin):
    user = ForeignKey(UserHealPoint, on_delete=SET_NULL, related_name="patient", null=True) 
    is_default = BooleanField(default=False, verbose_name=_("Is default patient"))

    class Meta:
        verbose_name = _("patient")
        verbose_name_plural = _("patients")