"""bcg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from web.grafana.views import DashboardView
from web.ruuvitags.urls import router as ruuvitag_router

api_router = routers.DefaultRouter()
api_router.registry.extend(ruuvitag_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', DashboardView.as_view(), name='dashboard-view'),
    path('api/', include(api_router.urls)),
    path('api/specs/', get_schema_view(title='RuuviHub', version='0.0.1'), name='api-specs'),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/charts/', include('web.charts.urls')),
]
