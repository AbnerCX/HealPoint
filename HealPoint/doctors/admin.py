from django.contrib import admin

from .models import Doctor, ProffesionalLicence

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "professional_phone",
    )
    search_fields = ("names", "father_surname", "mother_surname")

@admin.register(ProffesionalLicence)
class ProffesionalLicenceAdmin(admin.ModelAdmin):
    list_display = (
        "doctor",
        "number",
        "expiration_date",
        "issuing_date"
    )