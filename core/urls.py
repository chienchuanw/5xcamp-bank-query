from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path("", include("banks.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
]
