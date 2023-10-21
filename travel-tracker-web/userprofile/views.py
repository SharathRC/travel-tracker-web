from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            UserProfile.objects.create(user=user)

            return redirect("homepage")
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})
