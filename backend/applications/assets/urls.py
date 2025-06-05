from rest_framework.routers import DefaultRouter
from .viewsets.metal_viewset import MetalViewSet

# from .viewsets import LeadsProfileViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r"metales", MetalViewSet, basename="activos")


urlpatterns = router.urls
