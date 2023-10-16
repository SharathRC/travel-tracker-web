from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from .views import homepage

urlpatterns = [
    path("", homepage, name="homepage"),
]
