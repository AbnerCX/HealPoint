from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "doctor", "store", "start_time", "end_time", "status")
    list_filter = ("doctor", "store", "status")