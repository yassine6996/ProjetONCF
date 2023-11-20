from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Train, Passenger, Reservation, Ticket, Payment, Station, Route, Amenities, Schedule, Discount, UserProfile
from .forms import ReservationForm, PassengerForm, TicketForm, PaymentForm, StationForm, RouteForm, AmenitiesForm, ScheduleForm, DiscountForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User  # Import User model
from django.core.mail import send_mail
from django.http import HttpResponse



# Views for Train model
def train_list(request):
    trains = Train.objects.all()
    return render(request, 'train_list.html', {'trains': trains})

def train_detail(request, train_id):
    train = get_object_or_404(Train, pk=train_id)
    return render(request, 'train_detail.html', {'train': train})

def search_trains(request):
    if request.method == 'GET':
        # Retrieve query parameters from the URL
        origin = request.GET.get('origin')
        destination = request.GET.get('destination')

        # Perform the search based on the provided criteria
        if origin and destination:
            # Query the database to find matching trains
            matching_trains = Train.objects.filter(origin=origin, destination=destination)
        else:
            # If criteria not provided, return all trains
            matching_trains = Train.objects.all()

        context = {
            'matching_trains': matching_trains,
            'origin': origin,
            'destination': destination,
        }

        return render(request, 'search_trains.html', context)
    
# Views for Passenger model
def passenger_list(request):
    passengers = Passenger.objects.all()
    return render(request, 'passenger_list.html', {'passengers': passengers})

def passenger_detail(request, passenger_id):
    passenger = get_object_or_404(Passenger, pk=passenger_id)
    return render(request, 'passenger_detail.html', {'passenger': passenger})

@login_required
def edit_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile was successfully updated.')
    else:
        form = UserProfileForm(instance=user_profile)
    
    return render(request, 'edit_profile.html', {'form': form, 'user_profile': user_profile})

# Views for Reservation model
def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation_list.html', {'reservations': reservations})

def reservation_detail(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    return render(request, 'reservation_detail.html', {'reservation': reservation})

@login_required
def make_reservation(request, train_id):
    train = get_object_or_404(Train, pk=train_id)
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.train = train
            reservation.save()
            messages.success(request, 'Reservation was successfully made.')
            return redirect('reservation_detail', reservation_id=reservation.id)
    else:
        form = ReservationForm()
    
    return render(request, 'make_reservation.html', {'form': form, 'train': train})


@login_required
def update_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation updated successfully!')
            return redirect('reservation_detail', reservation_id=reservation.id)
    else:
        form = ReservationForm(instance=reservation)

    context = {'form': form, 'reservation': reservation}
    return render(request, 'update_reservation.html', context)





@login_required
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    
    if request.user != reservation.passenger.user:
        raise PermissionDenied
    
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Reservation was successfully canceled.')
        return redirect('reservation_list')
    
    return render(request, 'cancel_reservation.html', {'reservation': reservation})




# Views for Ticket model
def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticket_list.html', {'tickets': tickets})

def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(request, 'ticket_detail.html', {'ticket': ticket})

@login_required
def create_ticket(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.reservation = reservation
            ticket.save()
            messages.success(request, 'Ticket created successfully!')
            return redirect('reservation_detail', reservation_id=reservation.id)
    else:
        form = TicketForm()

    context = {'form': form, 'reservation': reservation}
    return render(request, 'create_ticket.html', context)


# Views for Payment model




def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment_list.html', {'payments': payments})

def payment_detail(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    return render(request, 'payment_detail.html', {'payment': payment})



# Views for Station model
def station_list(request):
    stations = Station.objects.all()
    return render(request, 'station_list.html', {'stations': stations})

def station_detail(request, station_id):
    station = get_object_or_404(Station, pk=station_id)
    return render(request, 'station_detail.html', {'station': station})

# Views for Route model
def route_list(request):
    routes = Route.objects.all()
    return render(request, 'route_list.html', {'routes': routes})


def add_payment(request, reservation_id):
    # Get the reservation object using the reservation_id
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    if request.method == 'POST':
        # Handle the form submission
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Save the payment information to the reservation
            payment = form.save(commit=False)
            payment.reservation = reservation
            payment.save()

            # Redirect to a success page or perform further actions
            return redirect('payment_success')  # Redirect to a success page

    else:
        # Display the payment form
        form = PaymentForm()

    context = {
        'reservation': reservation,
        'form': form,
    }

    return render(request, 'add_payment.html', context)

def discount_list(request):
    # Retrieve all available discounts from the database
    discounts = Discount.objects.all()

    context = {'discounts': discounts}
    return render(request, 'discount_list.html', context)

def apply_discount(request, reservation_id):
    # Get the reservation object using the reservation_id
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    if request.method == 'POST':
        # Handle the form submission
        form = DiscountForm(request.POST)
        if form.is_valid():
            # Retrieve the discount code entered by the user
            discount_code = form.cleaned_data['discount_code']

            try:
                # Check if a discount with the provided code exists
                discount = Discount.objects.get(code=discount_code)

                # Apply the discount to the reservation (adjust the price as needed)
                reservation.apply_discount(discount)

                # Redirect to a success page or perform further actions
                return redirect('reservation_detail', reservation_id=reservation.id)

            except Discount.DoesNotExist:
                # Handle the case where the discount code is not valid
                form.add_error('discount_code', 'Invalid discount code')

    else:
        # Display the discount code entry form
        form = DiscountForm()

    context = {
        'reservation': reservation,
        'form': form,
    }

    return render(request, 'apply_discount.html', context)

def home(request):
    return render(request, 'pages/home.html', {})

def Capital_Humain(request):
    return render(request, 'pages/Entreprise/Capital_Humain.html', {})

def Transformation_digitale(request):
    return render(request, 'pages/Entreprise/Transformation_digitale.html', {})

def about(request):
    return render(request, 'pages/about.html', {})


def service(request):
    return render(request, 'pages/service.html', {})


def pricing(request):
    return render(request, 'pages/pricing.html', {})


def Profile_de_loncf(request):
    return render(request, 'pages/Entreprise/Profile_de_loncf.html', {})


def Entreprise(request):
    return render(request, 'pages/Entreprise/Entreprise.html', {})

def Gouvernance(request):
    return render(request, 'pages/Entreprise/Gouvernance.html', {})

def Missions_valeurs(request):
    return render(request, 'pages/Entreprise/Missions_valeurs.html', {})

def Filiale(request):
    return render(request, 'pages/Entreprise/Filiale.html', {})

def Engares(request):
    return render(request, 'pages/Voyageurs/Engares.html', {})

def Carte_smart_navette(request):
    return render(request, 'pages/Voyageurs/Carte_smart_navette.html', {})

def AlAtlas(request):
    return render(request, 'pages/Voyageurs/AlAtlas.html', {})

def Personne_mobilite_reduite(request):
    return render(request, 'pages/Voyageurs/Personne_mobilite_reduite.html', {})

def Charte_achats(request):
    return render(request, 'pages/Entreprise/Charte_achats.html', {})

def ONCF_trafic(request):
    return render(request, 'pages/Voyageurs/ONCF_trafic.html', {})

def Canneaux_de_vente(request):
    return render(request, 'pages/Voyageurs/Canneaux_de_vente.html', {})

def Carte_attalib(request):
    return render(request, 'pages/Voyageurs/Carte_attalib.html', {})

def Carte_jeune(request):
    return render(request, 'pages/Voyageurs/Carte_jeune.html', {})

def Carte_10ZEN(request):
    return render(request, 'pages/Voyageurs/Carte_10ZEN.html', {})

def Carte_senior(request):
    return render(request, 'pages/Voyageurs/Carte_senior.html', {})

def AlBoraq(request):
    return render(request, 'pages/AlBoraq/AlBoraq.html', {})

def Destinations(request):
    return render(request, 'pages/AlBoraq/Destinations.html', {})

def Informer_et_acheter(request):
    return render(request, 'pages/AlBoraq/Informer_et_acheter.html', {})

def Reservation(request):
    return render(request, 'pages/AlBoraq/Reservation.html', {})


def Service_en_gars(request):
    return render(request, 'pages/AlBoraq/Service_en_gars.html', {})



def Nosprix(request):
    return render(request, 'pages/AlBoraq/Nosprix.html', {})



def ServiceBord(request):
    return render(request, 'pages/AlBoraq/ServiceBord.html', {})

def Historique(request):
    return render(request, 'pages/Entreprise/Historique.html', {})

def Chiffre_cle(request):
    return render(request, 'pages/Entreprise/Chiffre_cle.html', {})

def Faire_carriere(request):
    return render(request, 'pages/Entreprise/Faire_carriere.html', {})

def Fret_logistique(request):
    return render(request, 'pages/Fret_et_logistique/Fret_logistique.html', {})

def Fret_Environnement(request):
    return render(request, 'pages/Fret_et_logistique/Fret_Environnement.html', {})

def Projet_en_cours(request):
    return render(request, 'pages/Fret_et_logistique/Projet_en_cours.html', {})

def Enquete_satisfaction_client(request):
    return render(request, 'pages/Fret_et_logistique/Enquete_satisfaction_client.html', {})

def Offres_logistique(request):
    return render(request, 'pages/Fret_et_logistique/Offres_logistique.html', {})

def Notre_offre_logistique(request):
    return render(request, 'pages/Fret_et_logistique/Notre_offre_logistique.html', {})
def Mita_casa(request):
    return render(request, 'pages/Fret_et_logistique/Mita_casa.html', {})


def Bensouda_Fes(request):
    return render(request, 'pages/Fret_et_logistique/Bensouda_Fes.html', {})

def Vision(request):
    return render(request, 'pages/Developpement/Vision.html', {})

def Axes_strategique(request):
    return render(request, 'pages/Developpement/Axes_strategique.html', {})

def Plan_rail(request):
    return render(request, 'pages/Developpement/Plan_rail.html', {})

def Projet_structurant(request):
    return render(request, 'pages/Developpement/Projet_structurant.html', {})

def Ligne_grande_vitesse(request):
    return render(request, 'pages/Developpement/Ligne_grande_vitesse.html', {})

def Triplement_casa_kenitra(request):
    return render(request, 'pages/Developpement/Triplement_casa_kenitra.html', {})

def Doublement_casa_marrakesh(request):
    return render(request, 'pages/Developpement/Doublement_casa_marrakesh.html', {})

def Securite_surete(request):
    return render(request, 'pages/Developpement/Securite_surete.html', {})

def Gares(request):
    return render(request, 'pages/Developpement/Gares.html', {})

def Desaturation(request):
    return render(request, 'pages/Developpement/Desaturation.html', {})

def Sidi_ghanem(request):
    return render(request, 'pages/Fret_et_logistique/Sidi_ghanem.html', {})



def Developpement(request):
    return render(request, 'pages/Developpement/Developpement.html', {})
       


def Missions(request):
    return render(request, 'pages/Fret_et_logistique/Missions.html', {})


def Atouts(request):
    return render(request, 'pages/Fret_et_logistique/Atouts.html', {})


def Fret_chiffres(request):
    return render(request, 'pages/Fret_et_logistique/Fret_chiffres.html', {})

def Transport_rail_route(request):
    return render(request, 'pages/Fret_et_logistique/Transport_rail_route.html', {})                                                                               



def Offre_transport_logistique(request):
    return render(request, 'pages/Fret_et_logistique/Offre_transport_logistique.html', {})


def Produit_chimique(request):
    return render(request, 'pages/Fret_et_logistique/Produit_chimique.html', {})


def Minerai_materiauxBTP(request):
    return render(request, 'pages/Fret_et_logistique/Minerai_materiauxBTP.html', {})


def Energie(request):
    return render(request, 'pages/Fret_et_logistique/Energie.html', {})


def Automobile(request):
    return render(request, 'pages/Fret_et_logistique/Automobile.html', {})


def Produit_agri_agro(request):
    return render(request, 'pages/Fret_et_logistique/Produit_agri_agro.html', {})     


def Voyagez_meilleur_prix(request):
    return render(request, 'pages/AlBoraq/Voyagez_meilleur_prix.html', {})



def Nos_abonnement(request):
    return render(request, 'pages/AlBoraq/Nos_abonnement.html', {})



def Voyagez_ptit_prix(request):
    return render(request, 'pages/AlBoraq/Voyagez_ptit_prix.html', {})



def contact(request):
    if request.method == "POST":
        message_name = request.POST.get('message_name', '')
        message_email = request.POST.get('message_email', '')
        message = request.POST.get('message', '')

        if message_name and message_email and message:
            # All required fields are present; send mail
            send_mail(
                message_name,
                message,
                message_email,
                ['yassine6996@gmail.com'],
            )

        return render(request, 'pages/contact.html')
    else:
        return render(request, 'pages/contact.html')



def blog(request):
    return render(request, 'pages/blog.html', {})


def blog_details(request):
    return render(request, 'pages/blog-details.html', {})