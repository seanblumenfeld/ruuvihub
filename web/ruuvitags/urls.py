from rest_framework.routers import SimpleRouter

from web.ruuvitags.views import (
    EventViewSet, SensorViewSet, LocationViewSet, BroadcastViewSet
)

router = SimpleRouter()
router.register('events', EventViewSet, basename='events')
router.register('locations', LocationViewSet, basename='locations')
router.register('sensors', SensorViewSet, basename='sensors')
router.register('broadcasts', BroadcastViewSet, basename='broadcasts')

urlpatterns = router.urls
