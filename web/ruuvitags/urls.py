from web.ruuvitags.views import EventViewSet, SensorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('events', EventViewSet, basename='events')
router.register('sensors', SensorViewSet, basename='sensors')
