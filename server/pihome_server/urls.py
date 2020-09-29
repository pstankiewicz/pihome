"""pihome_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from rest_framework import routers
from sensors import views

router = routers.DefaultRouter()
router.register(r"sensor-data", views.SensorDataViewSet)

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html")),
    path(
        "sensor-details/<uuid:pk>",
        views.SensorDetail.as_view(template_name="sensors/sensor-detail.html"),
        name="sensor-details",
    ),
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)