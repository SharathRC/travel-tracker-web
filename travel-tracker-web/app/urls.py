from django.contrib import admin
from django.urls import path, include

from .views import (
    trip_detail,
    add_new_trip,
)


urlpatterns = [
    path("trips/<slug:slug>/", trip_detail, name="trip_detail"),
    path("add-new-trip/", add_new_trip, name="add_trip"),
]
