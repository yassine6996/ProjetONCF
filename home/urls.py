from os import path
from .views import *
from . import views
from django.contrib import admin
from django.urls import  path

urlpatterns = [
   # List all available trains
        path('api/train_list/', views.train_list, name='train_list'),
         # View details of a specific train
        path('trains/<int:train_id>/', views.train_detail, name='train_detail'),

        # List all reservations
        path('reservations/', views.reservation_list, name='reservation_list'),

        # View details of a specific reservation
        path('reservations/<int:reservation_id>/', views.reservation_detail, name='reservation_detail'),

        # Make a new reservation for a specific train
        path('trains/<int:train_id>/reserve/', views.make_reservation, name='make_reservation'),

        # Cancel a reservation
        path('reservations/<int:reservation_id>/cancel/', views.cancel_reservation, name='cancel_reservation'),

        # List user's reservations (if you have user authentication)
        path('my_reservations/', views.make_reservation, name='my_reservations'),

        # View and edit user profile (if you have user authentication)
        path('profile/', views.edit_profile, name='edit_profile'),

   

        # Search for trains by criteria (e.g., origin and destination)
        path('search/', views.search_trains, name='search_trains'),

        # Add payment information for a reservation
        path('reservations/<int:reservation_id>/payment/', views.add_payment, name='add_payment'),

        # List available discounts and promotions
        path('discounts/', views.discount_list, name='discount_list'),

        # Apply a discount code to a reservation
        path('reservations/<int:reservation_id>/apply_discount/', views.apply_discount, name='apply_discount'),

        # Additional URLs for amenities, stations, routes, and schedules
        # ...
        path('stations/', views.station_list, name='station_list'),

        # Admin-specific URLs (if needed)
        path('admin/', admin.site.urls),  # Already defined in your project's main URLs

        # Homepage or landing page
        path('home', views.home, name='home'),
        path('', views.Entreprise, name='Entreprise'),
        path('about', views.about, name='about'),
        path('service', views.service, name='service'),
        path('pricing', views.pricing, name='pricing'),
        path('contact', views.contact, name='contact'),
        path('blog', views.blog, name='blog'),
        path('blog-details', views.blog_details, name='blog_details'),
        path('Entreprise', views.Entreprise, name='Entreprise'),
        path('Profile_de_loncf', views.Profile_de_loncf, name='Profile_de_loncf'),
        path('Missions_valeurs', views.Missions_valeurs, name='Missions_valeurs'),
        path('Gouvernance', views.Gouvernance, name='Gouvernance'),
        path('Historique', views.Historique, name='Historique'),
        path('Faire_carriere', views.Faire_carriere, name='Faire_carriere'),
        path('AlBoraq', views.AlBoraq, name='AlBoraq'),
        path('Destinations', views.Destinations, name='Destinations'),
        path('Informer_et_acheter', views.Informer_et_acheter, name='Informer_et_acheter'),
        path('Reservation', views.Reservation, name='Reservation'),
        path('Service_en_gars', views.Service_en_gars, name='Service_en_gars'),
        path('ServiceBord', views.ServiceBord, name='ServiceBord'),
        path('Nosprix', views.Nosprix, name='Nosprix'),
        path('Fret_logistique', views.Fret_logistique, name='Fret_logistique'),

        path('Enquete_satisfaction_client', views.Enquete_satisfaction_client, name='Enquete_satisfaction_client'),  
        path('Fret_Environnement', views.Fret_Environnement, name='Fret_Environnement'),
        path('Projet_en_cours', views.Projet_en_cours, name='Projet_en_cours'),
        path('Offres_logistique', views.Offres_logistique, name='Offres_logistique'),
        path('Notre_offre_logistique', views.Notre_offre_logistique, name='Notre_offre_logistique'),
        path('Mita_casa', views.Mita_casa, name='Mita_casa'),
        path('Bensouda_Fes', views.Bensouda_Fes, name='Bensouda_Fes'),
        path('Sidi_ghanem', views.Sidi_ghanem, name='Sidi_ghanem'),
        path('Vision', views.Vision, name='Vision'),
        path('Axes_strategique', views.Axes_strategique, name='Axes_strategique'),
        path('Plan_rail', views.Plan_rail, name='Plan_rail'),
        path('Projet_structurant', views.Projet_structurant, name='Projet_structurant'),
        path('Ligne_grande_vitesse', views.Ligne_grande_vitesse, name='Ligne_grande_vitesse'),
        path('Triplement_casa_kenitra', views.Triplement_casa_kenitra, name='Triplement_casa_kenitra'),
        path('Doublement_casa_marrakesh', views.Doublement_casa_marrakesh, name='Doublement_casa_marrakesh'),
        path('Securite_surete', views.Securite_surete, name='Securite_surete'),
        path('Gares', views.Gares, name='Gares'),
        path('Desaturation', views.Desaturation, name='Desaturation'),
        path('Chiffre_cle', views.Chiffre_cle, name='Chiffre_cle'),
        path('Capital_Humain', views.Capital_Humain, name='Capital_Humain'),     
        path('Transformation_digitale', views.Transformation_digitale, name='Transformation_digitale'), 
        path('Missions', views.Missions, name='Missions'),
        path('Atouts', views.Atouts, name='Atouts'),
        path('Fret_chiffres', views.Fret_chiffres, name='Fret_chiffres'),
        path('Transport_rail_route', views.Transport_rail_route, name='Transport_rail_route'),
        path('Carte_senior', views.Carte_senior, name='Carte_senior'),
        path('Carte_jeune', views.Carte_jeune, name='Carte_jeune'),
        path('Carte_attalib', views.Carte_attalib, name='Carte_attalib'),
        path('Engares', views.Engares, name='Engares'),
        path('Carte_10ZEN', views.Carte_10ZEN, name='Carte_10ZEN'),
        path('AlAtlas', views.AlAtlas, name='AlAtlas'),
        path('Canneaux_de_vente', views.Canneaux_de_vente, name='Canneaux_de_vente'),
        path('Filiale', views.Filiale, name='Filiale'),
        path('ONCF_trafic', views.ONCF_trafic, name='ONCF_trafic'),
        path('Personne_mobilite_reduite', views.Personne_mobilite_reduite, name='Personne_mobilite_reduite'),
        path('Charte_achats', views.Charte_achats, name='Charte_achats'),



        path('Carte_smart_navette', views.Carte_smart_navette, name='Carte_smart_navette'),
        path('Offre_transport_logistique', views.Offre_transport_logistique, name='Offre_transport_logistique'),
        path('Produit_chimique', views.Produit_chimique, name='Produit_chimique'),
        path('Minerai_materiauxBTP', views.Minerai_materiauxBTP, name='Minerai_materiauxBTP'),
        path('Energie', views.Energie, name='Energie'),
        path('Produit_agri_agro', views.Produit_agri_agro, name='Produit_agri_agro'),     
        path('Automobile', views.Automobile, name='Automobile'),

        path('Voyagez_meilleur_prix', views.Voyagez_meilleur_prix, name='Voyagez_meilleur_prix'),
        path('Nos_abonnement', views.Nos_abonnement, name='Nos_abonnement'),
        path('Voyagez_ptit_prix', views.Voyagez_ptit_prix, name='Voyagez_ptit_prix'),

        path('Developpement', views.Developpement, name='Developpement'),











]
