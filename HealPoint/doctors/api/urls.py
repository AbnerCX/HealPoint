from django.urls import path, include
from rest_framework.routers import DefaultRouter
from doctors.api.views import DoctorViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctor')

urlpatterns = [
    path('', include(router.urls)),
]
