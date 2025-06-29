from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.mixins import (
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from doctors.api.serializers import DoctorSerializer
from doctors.models import Doctor

class DoctorViewSet(
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    """
    API endpoint that allows doctors to be viewed or edited.
    """

    queryset = Doctor.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = DoctorSerializer

    @action(detail=False, methods=["get"], url_path="by-user-phone/(?P<phone_number>[^/]+)",)
    def get_by_user_phone(self, request:Request, phone_number: str) -> Response:
        obj = get_object_or_404(Doctor, user__phone_number=phone_number)
        serializer = self.get_serializer(obj)
        return Response(data=serializer.data)