from django import forms
from .models import Trip


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ["title", "start_trip", "end_trip", "cover_image"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 my-2 border border-gray-200",
                }
            ),
            "start_trip": forms.SelectDateWidget(
                attrs={
                    "class": "mx-4 px-3 py-2 my-2 border border-gray-200",
                },
                empty_label=("Choose Year", "Choose Month", "Choose Day"),
            ),
            "end_trip": forms.SelectDateWidget(
                attrs={
                    "class": "mx-4 px-3 py-2 my-2 border border-gray-200",
                },
                empty_label=("Choose Year", "Choose Month", "Choose Day"),
            ),
            "cover_image": forms.FileInput(
                attrs={
                    "class": "w-full px-3 py-2 my-2 border border-gray-200",
                }
            ),
        }
