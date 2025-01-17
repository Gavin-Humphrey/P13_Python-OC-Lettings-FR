from django.contrib import admin
from django.urls import path, include
from .views import trigger_error


urlpatterns = [
    path("", include("homepage.urls")),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
    path("sentry-debug/", trigger_error),
]
