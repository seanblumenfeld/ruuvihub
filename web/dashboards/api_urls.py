from django.urls import path

from web.dashboards.views import TemperatureChartDataView

app_name = 'dashboards-api'

urlpatterns = [
    path('charts/data', TemperatureChartDataView.as_view(), name='charts-data-temperature'),
]
