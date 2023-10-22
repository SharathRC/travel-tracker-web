from django.shortcuts import render, get_object_or_404, redirect

from .models import Trip


def trip_detail(request, slug):
    trip = get_object_or_404(Trip, slug=slug, status=Trip.ACTIVE)
    context = {"trip": trip}

    return render(request, "trip_detail.html", context)
