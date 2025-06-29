from rest_framework.serializers import CharField, ModelSerializer

from doctors.models import Doctor

class DoctorSerializer(ModelSerializer[Doctor]):
    gender_display = CharField(source = "get_gender_display")
    nationality_display = CharField(source = "get_nationality_display")

    class Meta:
        model = Doctor
        read_only = (
            "id",
            "gender_display",
            "nationality_display",
            "created_at",
            "updated_at",
        )
        fields = "__all__"