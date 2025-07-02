from django.db.models import (
    ForeignKey,
    PositiveSmallIntegerField,
    DateTimeField,
    TextField,
    CASCADE,
    SET_NULL,


)

from django.utils.translation import gettext_lazy as _

from helpers.model_mixins import BaseMetaMixin
from constants.appointment_status import AppointmentStatus

from patients.models import Patient
from doctors.models import Doctor
from stores.models import Store

class Appointment(BaseMetaMixin):
    patient = ForeignKey(Patient, on_delete=CASCADE, related_name="appointments")
    doctor = ForeignKey(Doctor, on_delete=CASCADE, related_name="appointments")
    store = ForeignKey(Store, on_delete=SET_NULL, null=True, blank=True)

    start_time = DateTimeField(_("start time"))
    end_time = DateTimeField(_("end time"))

    status = PositiveSmallIntegerField(
        choices=AppointmentStatus.choices,
        default=AppointmentStatus.PENDING,
        verbose_name=_("status")
    )

    notes = TextField(_("notes"), blank=True)

    class Meta:
        verbose_name = _("Appointment")
        verbose_name_plural = _("Appointments")

    def __str__(self):
        return f"{self.patient} - {self.doctor} @ {self.start_time}"