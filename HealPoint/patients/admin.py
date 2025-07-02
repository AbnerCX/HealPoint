from django.contrib import admin

from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    search_fields = ("names", "father_surname", "mother_surname",)
    list_display =("full_name", "age", "birth_date", "gender", "created_at")