from django import forms
from .models import Reservation, Passenger, Ticket, Payment, Station, Route, Amenities, Schedule, Discount, UserProfile
from django.contrib.auth.models import User

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['train', 'passenger', 'seat_numbers']
        # You can customize the form widgets, labels, and more as needed

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['first_name', 'last_name', 'email']
        # Customize the form as needed

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['reservation', 'ticket_number', 'price', 'seat_number', 'passenger']
        # Customize the form as needed

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['reservation',  'amount', 'payment_method']
        # Customize the form as needed


class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['name', 'code']
        # Customize the form as needed

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['train', 'origin', 'destination']
        # Customize the form as needed

class AmenitiesForm(forms.ModelForm):
    class Meta:
        model = Amenities
        fields = ['name', 'description']
        # Customize the form as needed

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['train', 'station', 'departure_time', 'arrival_time']
        # Customize the form as needed

class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ['name', 'code', 'percentage', 'expiration_date']
        # Customize the form as needed

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'phone_number', 'date_of_birth']
        # Customize the form as needed
