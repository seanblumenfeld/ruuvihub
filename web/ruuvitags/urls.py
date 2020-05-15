from rest_framework.routers import SimpleRouter

from web.ruuvitags.views import EventViewSet, SensorViewSet

router = SimpleRouter()
router.register('events', EventViewSet, basename='events')
router.register('sensors', SensorViewSet, basename='sensors')
