from django.db import models
from django.contrib.auth.models import User


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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)

    class Meta:
        verbose_name_plural = "Trips"
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.title
