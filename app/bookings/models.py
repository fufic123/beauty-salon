from django.db import models
from services.models import Service

class Booking(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    time = models.TimeField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('date', 'time', 'service')  # Доп. защита от дублей

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.service.name} on {self.date} at {self.time}"
