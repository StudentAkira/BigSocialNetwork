from users.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'get', UserViewSet, basename='user')
urlpatterns = router.urls
