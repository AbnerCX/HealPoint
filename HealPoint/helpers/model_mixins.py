import uuid
from datetime import datetime

import pytz
from django.db.models import (
    DateField,
    DateTimeField,
    IntegerField,
    PositiveIntegerField,
    Model,
    TextField,
    UUIDField,
)

from django.utils.translation import gettext_lazy as _
from django.utils.functional import cached_property
from django.db.models import IntegerChoices

from constants.locations import (
    MexicanStates,
    Countries,
    Nationalities,
)


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
    
class AddressMixin(BaseMetaMixin):
    street = TextField(_("street"), max_length=155, blank=True)
    number = TextField(_("number"), max_length=50, blank=True)
    neighborhood = TextField(_("neighborhood"), max_length=155)
    city = TextField(_("city"), max_length=155)
    state = IntegerField(
        _("state"),
        choices=MexicanStates.choices,
        default=MexicanStates.JALISCO,
        db_index=True,
    )
    country = IntegerField(
        _("country"),
        choices=Countries.choices,
        default=Countries.MEXICO,
        db_index=True,
    )
    zip_code = PositiveIntegerField(_("zip code"), null=True, blank=True, db_index=True)

    class Meta(BaseMetaMixin.Meta):
        abstract = True

    @cached_property
    def full_address(self) -> str:
        return (
            f"{self.street} {self.number}, {self.neighborhood}, {self.city}, "
            f"{self.state}, {self.country}, {self.zip_code or ''}"
        ).strip()