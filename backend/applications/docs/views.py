from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Documentación"])
class CustomSpectacularAPIView(SpectacularAPIView):
    pass


# Create your views here.
