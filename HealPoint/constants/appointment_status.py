from django.utils.translation import gettext_lazy as _
from django.db.models import IntegerChoices

class AppointmentStatus(IntegerChoices):
    PENDING = 1, _("Pending")
    CONFIRMED = 2, _("Confirmed")
    CANCELLED = 3, _("Cancelled")
    COMPLETED = 4, _("Completed")
