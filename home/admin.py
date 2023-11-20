from django.contrib import admin
from .models import Train, Passenger, Reservation, Ticket, Payment, Station, Route, Amenities, Schedule, Discount, TrainCategory, UserProfile



class TrainAdmin(admin.ModelAdmin):
    list_display = ('train_number', 'name', 'origin', 'destination', 'departure_time', 'arrival_time', 'total_seats', 'available_seats')
    list_filter = ('origin', 'destination')
    search_fields = ('name', 'train_number')



class ReservationAdmin(admin.ModelAdmin):
    list_display = ('passenger', 'train', 'reservation_date', 'seat_numbers')
    list_filter = ('seat_numbers',)
    search_fields = ('passenger__name', 'train__name')  # Replace with actual field names

class TicketInline(admin.TabularInline):
    model = Ticket
    extra = 1

class PassengerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'email' )
    search_fields = ('first_name','last_name', 'email')
    inlines = [TicketInline]

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'amount', 'payment_date', 'payment_method')
    list_filter = ('payment_method',)
    search_fields = ('reservation__passenger__name',)

class TrainCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

# Register your models with their respective admin classes
admin.site.register(Train, TrainAdmin)
admin.site.register(Passenger, PassengerAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Ticket)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Station)
admin.site.register(Route)
admin.site.register(Amenities)
admin.site.register(Schedule)
admin.site.register(Discount)
admin.site.register(UserProfile)
admin.site.register(TrainCategory)






# Register your models here.
