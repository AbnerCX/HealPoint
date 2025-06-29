from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from drf_spectacular.utils import extend_schema, extend_schema_view
from django.urls import path, include
from django.contrib import admin

@extend_schema_view(get=extend_schema(exclude=True))

class HiddenSchemaView(SpectacularAPIView):
    pass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.api.urls')),
    path('api/', include('doctors.api.urls')),

    path('api/schema/', HiddenSchemaView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
