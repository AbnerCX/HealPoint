from drf_spectacular.utils import extend_schema, OpenApiResponse
from .serializers import UserSerializer

get_me_schema = extend_schema(
    summary="Get authenticated user profile",
    description="Returns the data of the currently authenticated user.",
    responses={
        200: OpenApiResponse(response=UserSerializer, description="Authenticated user profile"),
        401: OpenApiResponse(description="Not authenticated or invalid token"),
    },
    tags=["users"]
)
