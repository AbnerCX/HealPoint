from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import PatientSerializer
from patients.models import Patient



class PatientViewSet(ModelViewSet):
    """
    API endpoint that allows patients to be viewed or edited.
    """

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Exclude patients without a user.
        This is useful for filtering out patients that are not associated with any user.
        """
        return super().get_queryset().exclude(user=None)