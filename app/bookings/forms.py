from django import forms
from .models import Booking
from datetime import datetime, timedelta
from services.models import Service

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'date', 'time', 'first_name', 'last_name', 'email', 'phone']

    def clean(self):
        cleaned_data = super().clean()
        service = cleaned_data.get('service')
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if not (service and date and time):
            return

        # Начало и конец процедуры с учётом перерыва
        start_time = datetime.combine(date, time)
        end_time = start_time + service.duration + timedelta(minutes=15)

        existing_bookings = Booking.objects.filter(service=service, date=date)

        for booking in existing_bookings:
            existing_start = datetime.combine(booking.date, booking.time)
            existing_end = existing_start + booking.service.duration + timedelta(minutes=15)

            # Проверка пересечений
            if (start_time < existing_end) and (end_time > existing_start):
                raise forms.ValidationError("Выбранное время занято или слишком близко к другой записи. Выберите другое время.")
