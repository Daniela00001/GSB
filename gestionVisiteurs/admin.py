from django.contrib import admin
from .models import Utilisateur, Rapport,Medecin,Medicament

class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ['id','nom', 'prenom', 'adresse', 'complement_adresse','ville', 'code_postal', 'email', 'numero_telephone', 'date_embauche', 'login', 'mot_de_passe']

class RapportAdmin(admin.ModelAdmin):
    list_display = ['date','motif', 'bilan','quantite','createur','medecin','medicament']

class MedecinAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'prenom', 'adresse', 'numero_telephone', 'specialisteComplimentaire', 'departement']

class MedicamentnAdmin(admin.ModelAdmin):
    list_display = ['id', 'nomCommercial', 'composition', 'effets', 'contreIndications']

admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(Rapport, RapportAdmin)
admin.site.register(Medecin, MedecinAdmin)
admin.site.register(Medicament, MedicamentnAdmin)
