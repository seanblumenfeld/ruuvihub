from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from web.ruuvitags.views import EventViewSet, SensorViewSet, LocationViewSet, BroadcastCreateView

router = SimpleRouter()
router.register('events', EventViewSet, basename='events')
router.register('locations', LocationViewSet, basename='locations')
router.register('sensors', SensorViewSet, basename='sensors')

urlpatterns = [
    url(r'^broadcasts/$', BroadcastCreateView.as_view(), name='broadcasts'),
] + router.urls
