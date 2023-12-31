from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from django.contrib import messages

import random
import string

from .models import Trip
from .forms import TripForm


ALPHA_NUM_LEN = 5


def trip_detail(request, slug):
    trip = get_object_or_404(Trip, slug=slug)
    context = {"trip": trip}

    return render(request, "trip_detail.html", context)


def add_new_trip(request):
    if request.method == "POST":
        form = TripForm(request.POST, request.FILES)

        if form.is_valid():
            trip_id = "".join(
                random.choice(string.ascii_lowercase + string.digits)
                for _ in range(ALPHA_NUM_LEN)
            )

            title = request.POST.get("title")

            trip = form.save(commit=False)
            trip.user = request.user

            slug = f"{trip.user}-{trip_id}-{title}"
            trip.slug = slugify(slug)
            trip.save()

            messages.success(request, "Trip added successfully!")

            return redirect("homepage")
    else:
        form = TripForm()

    context = {
        "title": "Add Trip",
        "form": form,
    }

    return render(request, "add_trip.html", context)
