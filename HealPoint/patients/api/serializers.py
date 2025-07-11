from rest_framework.serializers import ModelSerializer

from patients.models import Patient


class PatientSerializer(ModelSerializer[Patient]):
    class Meta:
        model = Patient
        read_only_fields = ("id", "age", "created_at", "full_name")
        fields = (
            "id",
            "user",
            "created_at",
            "birth_date",
            "age",
            "gender",
            "nationality",
            "full_name",
            "names",
            "father_surname",
            "mother_surname",
        )