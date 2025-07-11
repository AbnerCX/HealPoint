from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)

from users.models import UserHealPoint
from .serializers import UserSerializer, RegisterSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema

from .schemas import get_me_schema  

@extend_schema_view(
    list=extend_schema(tags=["users"]),
    retrieve=extend_schema(tags=["users"]),
    create=extend_schema(tags=["users"]),
    update=extend_schema(tags=["users"]),
    partial_update=extend_schema(tags=["users"])
)
class UserViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = UserHealPoint.objects.all()
    lookup_field = "pk"

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == "create":
            return RegisterSerializer
        return UserSerializer

    @get_me_schema 
    @action(
        detail=False,
        methods=["get"],
        url_path="me",
        permission_classes=[IsAuthenticated]
    )
    def get_me(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)
