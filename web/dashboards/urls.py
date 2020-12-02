from django.urls import path

from web.dashboards.views import DashboardRedirectView, ChartsTemplateView

app_name = 'dashboards'

urlpatterns = [
    path('<tag>/', DashboardRedirectView.as_view(), name='dashboard'),
    path('charts/1/', ChartsTemplateView.as_view(), name='charts-view'),
]
