from django.shortcuts import render

from app.models import Trip


def homepage(request):
    # products = Trip.objects.filter(status=Trip.ACTIVE)
    trips = Trip.objects.all()
    context = {"trips": trips}

    return render(request, "homepage.html", context)
