from users.views import UserViewSet, SubscribersViewSet, TestView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'all', TestView, basename='')
urlpatterns = router.urls
