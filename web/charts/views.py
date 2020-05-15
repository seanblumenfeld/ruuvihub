from django.shortcuts import render
from django.utils import timezone
from django.views import View
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from web.charts.serializers import TemperatureChartDataSerializer
from web.ruuvitags.models import Event


class ChartsTemplateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'chart.html')


class TemperatureChartDataView(GenericAPIView):
    queryset = Event.objects.filter(created__gte=timezone.now() - timezone.timedelta(days=1))
    serializer_class = TemperatureChartDataSerializer
    filterset_fields = ['sensor']

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
