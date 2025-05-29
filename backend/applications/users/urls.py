from rest_framework.routers import DefaultRouter
from .viewsets.user_register import UserRegistrationViewSet
from .viewsets.user_management import UserViewSet
from .viewsets.user_login import LoginViewSet

# from .viewsets import LeadsProfileViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r"register", UserRegistrationViewSet, basename="user-register")
router.register(r"users-management", UserViewSet, basename="users")
router.register(r"auth", LoginViewSet, basename="login")


urlpatterns = router.urls
