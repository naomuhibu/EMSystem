from rest_framework.routers import DefaultRouter

from .views import EarthquakeViewSet

router = DefaultRouter()

router.register(prefix='api/v1/schools',
                viewset=EarthquakeViewSet, basename='earthquake')

urlpatterns = router.urls