from users.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'all', UserViewSet, basename='')

urlpatterns = router.urls
