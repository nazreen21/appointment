from django.db import models


class Appointment(models.Model):

    STATUS_CHOICES = [
        ("scheduled", "Scheduled"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    customer_name = models.CharField(max_length=120)
    customer_email = models.EmailField()

    appointment_datetime = models.DateTimeField()

    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="scheduled")

    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.customer_name} - {self.status}"