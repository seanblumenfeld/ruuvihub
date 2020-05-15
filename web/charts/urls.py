from django.urls import path
from web.charts.views import ChartsTemplateView, TemperatureChartDataView

urlpatterns = [
    path('', ChartsTemplateView.as_view(), name='charts-view'),
    path('data/temperature', TemperatureChartDataView.as_view(), name='chart-data-temp-view'),
]
