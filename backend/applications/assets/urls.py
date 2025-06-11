from rest_framework.routers import DefaultRouter
from .viewsets.metal_viewset import MetalViewSet
from .viewsets.coin_banknote_viewset import CoinBankNoteViewSet

# from .viewsets import LeadsProfileViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r"metales", MetalViewSet, basename="metals")
router.register(r"coins", CoinBankNoteViewSet, basename="coins")


urlpatterns = router.urls
