from django.db import models
from django.contrib.auth.models import User

class TrainCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name



class Train(models.Model):
    train_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    total_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()
    category = models.ForeignKey(TrainCategory, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"{self.train_number} - {self.name}"




class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    # Add more fields as needed

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Reservation(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)
    seat_numbers = models.CharField(max_length=50)
    # Add more fields as needed

    def __str__(self):
        return f"Reservation for {self.passenger} on {self.train}"

class Ticket(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=20, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seat_number = models.CharField(max_length=10)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, default=None)
    # Add more ticket-related fields as needed

class Payment(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    # Add more payment-related fields as needed


class Station(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self) -> str:
        return self.name
    # Add more station-related fields as needed

class Route(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    origin = models.ForeignKey(Station, related_name='origin_routes', on_delete=models.CASCADE)
    destination = models.ForeignKey(Station, related_name='destination_routes', on_delete=models.CASCADE)
    # Add more route-related fields as needed


class Amenities(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Schedule(models.Model):
    train = models.ForeignKey('Train', on_delete=models.CASCADE)
    station = models.ForeignKey('Station', on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return f"{self.train} - {self.station}"

class Discount(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    expiration_date = models.DateField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)  # Add 'date_of_birth' field
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Add 'phone_number' field
    # Add additional user-related fields as needed
    # For example, you can include fields like 'phone_number', 'date_of_birth', etc.

    def __str__(self):
        return self.user.username
    






