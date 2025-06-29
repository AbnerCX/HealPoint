import uuid
from datetime import datetime

import pytz
from django.db.models import (
    DateField,
    DateTimeField,
    IntegerField,
    Model,
    TextField,
    UUIDField,
)

from django.utils.translation import gettext_lazy as _
from django.utils.functional import cached_property
from django.db.models import IntegerChoices

class BaseMetaMixin(Model):
    id = UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    created_at = DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        abstract = True


class Gender(IntegerChoices):
    NOT_SPECIFIED = 0, _("Not Specified")
    MALE = 1, _("Male")
    FEMALE = 2, _("Female")
    OTHER = 3, _("Other")


class Nationalities(IntegerChoices):
    MEXICAN = 1, _("Mexican")
    AMERICAN = 2, _("American")
    OTHER = 3, _("Other")


class PersonMixin(BaseMetaMixin):
    names = TextField(_("names"), max_length=155, blank=True)
    father_surname = TextField(_("father surname"), max_length=155, blank=True)
    mother_surname = TextField(_("mother surname"), max_length=155, blank=True)
    birth_date = DateField(_("birth date"))
    gender = IntegerField(_("gender"), choices=Gender.choices)
    nationality = IntegerField(
        _("nationality"),
        choices=Nationalities.choices,
        default=Nationalities.MEXICAN,
    )

    class Meta(BaseMetaMixin.Meta):
        abstract = True
    
    def __str__(self) -> str:
        return self.full_name

    @cached_property
    def full_name(self) -> str:
        return f"{self.names} {self.father_surname} {self.mother_surname}"
    
    @cached_property
    def age(self) -> int:
        today = datetime.now(tz=pytz.utc)
        return (
            today.year
            - self.birth_date.year
            - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        )