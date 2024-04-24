from django.contrib import admin
from django.urls import path
from gestionVisiteurs.views import home_view,connexion_view,inscription_view,v_accueil,v_rapports,v_profil,deconnexion_view,v_affiche_mes_rapports,v_ajoutMedecin,v_ajoutMedicament,supprimer_rapport,modifier_rapport,supprimer_medecin,modifier_medecin,v_affiche_mes_medecins,v_affiche_mes_medicaments,modifier_medicament,supprimer_medicament,modifier_profil,supprimer_profil,rapport_search,medecin_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('v_accueil/', v_accueil, name='v_accueil'),
    path('v_ajoutMedecin/', v_ajoutMedecin, name='v_ajoutMedecin'),
    path('v_afficheMesMedecins/', v_affiche_mes_medecins, name='v_afficheMesMedecins'),
    path('v_ajoutMedicament/', v_ajoutMedicament, name='v_ajoutMedicament'),
    path('v_rapports/', v_rapports, name='v_rapports'),
    path('v_afficheMesRapports/', v_affiche_mes_rapports, name='v_afficheMesRapports'),
    path('v_afficheMesMedicament/', v_affiche_mes_medicaments, name='v_afficheMesMedicament'),
    path('v_profil/', v_profil, name='v_profil'),
    path('connexion/', connexion_view, name='connexion'),
    path('deconnexion/', deconnexion_view, name='deconnexion_view'),
    path('inscription/', inscription_view, name='inscription'),
    path('rapport/supprimer/<int:rapport_id>/', supprimer_rapport, name='supprimer_rapport'),
    path('utilisateur/supprimer/<int:utilisateur_id>/', supprimer_profil, name='supprimer_profil'),
    path('rapport_search/', rapport_search, name='rapport_search'),
    path('recherche_medecin/', medecin_search, name='recherche_medecin'),

    



    path('medecin/supprimer/<int:medecin_id>/', supprimer_medecin, name='supprimer_medecin'),
    path('medicament/supprimer/<int:medicament_id>/', supprimer_medicament, name='supprimer_medicament'),
    path('rapport/modifier/<int:rapport_id>/', modifier_rapport, name='modifier_rapport'),
    path('medecin/modifier/<int:medecin_id>/', modifier_medecin, name='modifier_medecin'),
    path('medicament/modifier/<int:medicament_id>/', modifier_medicament, name='modifier_medicament'),
    path('utilisateur/modifier/<int:utilisateur_id>/', modifier_profil, name='modifier_profil'),
]
