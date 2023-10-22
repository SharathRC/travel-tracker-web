from django.contrib import admin
from django.urls import path, include

from .views import trip_detail


urlpatterns = [
    path("trips/<slug:slug>/", trip_detail, name="trip_detail"),
]
