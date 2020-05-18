from django.urls import path

from web.dashboard.views import DashboardView, ChartsTemplateView, TemperatureChartDataView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard-view'),
    path('charts/', ChartsTemplateView.as_view(), name='charts-view'),
    path('charts/data', TemperatureChartDataView.as_view(), name='chart-data-temp-view'),

]
