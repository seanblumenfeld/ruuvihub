from web.ruuvitags.views import EventViewSet, SensorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(EventViewSet.url_prefix, EventViewSet)
router.register(SensorViewSet.url_prefix, SensorViewSet)
