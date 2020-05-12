from constance import config
from django.conf import settings
from django.shortcuts import redirect
from django.views import View
from grafana_api import GrafanaFace


class DashboardView(View):

    def get(self, request, *args, **kwargs):
        url = request.build_absolute_uri()
        url = url.replace(request.get_port(), settings.GRAFANA_PORT)

        grafana_api = GrafanaFace(
            auth=config.GRAFANA_API_KEY, host='grafana', port=settings.GRAFANA_PORT
        )
        # Search dashboards based on tag
        dashboards = grafana_api.search.search_dashboards(tag='flt', limit=1)

        if not dashboards:
            dashboards = grafana_api.search.search_dashboards(limit=1)

        if dashboards:
            dashboard = dashboards[0]
        else:
            dashboard = {}

        url = url.replace(request.path, dashboard.get('url', ''))
        return redirect(url)
