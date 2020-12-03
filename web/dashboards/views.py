from constance import config
from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView
from grafana_api import GrafanaFace
from rest_framework.generics import ListAPIView

from web.dashboards.serializers import TemperatureChartDataSerializer
from web.ruuvitags.models import Event


class TemperatureChartDataView(ListAPIView):
    queryset = Event.objects.filter(created__gte=timezone.now() - timezone.timedelta(days=1))
    serializer_class = TemperatureChartDataSerializer
    filterset_fields = ['location']


class ChartsTemplateView(TemplateView):
    template_name = 'chart.html'


class DashboardRedirectView(View):

    def get(self, request, tag):
        grafana_api = GrafanaFace(
            auth=config.GRAFANA_API_KEY, host='grafana', port=settings.GF_SERVER_HTTP_PORT
        )
        # Search dashboards based on tag
        kwargs = {'tag': tag, 'limit': 1}
        dashboard = grafana_api.search.search_dashboards(**kwargs)

        if dashboard:
            url = request.build_absolute_uri()
            url = url.replace(request.get_port(), settings.GF_SERVER_HTTP_PORT)
            url = url.replace(request.path, dashboard.get('url', ''))
            return redirect(url)

        raise Http404(f'Dashboard with tag {tag} not found.')
