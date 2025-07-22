from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.create_booking, name='create_booking'),
    path('success/', lambda request: render(request, 'bookings/success.html'), name='booking_success'),
]
