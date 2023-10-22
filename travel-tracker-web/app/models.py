from django.db import models
from django.contrib.auth.models import User
from django.core.files import File

from io import BytesIO
from PIL import Image


class Trip(models.Model):
    SCHEDULED = "scheduled"
    ACTIVE = "active"
    COMPLETED = "completed"
    DELETED = "deleted"

    STATUS_CHOICES = (
        (SCHEDULED, "Scheduled"),
        (ACTIVE, "Active"),
        (COMPLETED, "Completed"),
        (DELETED, "Deleted"),
    )
    user = models.ForeignKey(User, related_name="trips", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    description = models.TextField(blank=True)

    cover_image = models.ImageField(
        upload_to="uploads/trip_images/", blank=True, null=True
    )

    cover_thumbnail = models.ImageField(
        upload_to="uploads/trip_images/thumbnails/", blank=True, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)

    class Meta:
        verbose_name_plural = "Trips"
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.title

    def get_thumbnail(self):
        if self.cover_thumbnail:
            return self.cover_thumbnail.url

        if self.cover_image:
            self.cover_thumbnail = self.make_thumbnail(image=self.cover_image)
            self.save()

            return self.cover_thumbnail.url

        return "https://via.placehold.com/240x240x.jpg"

    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size, Image.Resampling.NEAREST)

        thumb_io = BytesIO()
        img.save(thumb_io, "JPEG", quality=80)

        name = image.name.replace("uploads/product_images/", "")
        thumbnail = File(thumb_io, name=name)

        return thumbnail

    def update_thumbnail(self):
        self.cover_thumbnail = self.make_thumbnail(image=self.cover_image)
        self.save()
