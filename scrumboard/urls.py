from scrumboard.api import CardViewSet, ListViewSet,RegisterView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Lists', ListViewSet)
router.register(r'cards', CardViewSet)
router.register(r'register', RegisterView)


urlpatterns = router.urls