
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import InscriptionForm, ConnexionForm,InscriptionFormRapport,InscriptionFormMedecin,InscriptionFormMedicament,InscriptionFormRapportMedecin,RapportSearchForm,MedecinSearchForm
from django.http import HttpResponse
from .models import Utilisateur,Rapport,Medecin,Medicament
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import DateField


from django.shortcuts import render


from datetime import datetime
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models.functions import Cast


def home_view(request):
    return render(request, 'home.html')








def inscription_view(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            # Vérifier si l'email, le numéro de téléphone ou le login existent déjà
            email = form.cleaned_data['email']
            numero_telephone = form.cleaned_data['numero_telephone']
            login = form.cleaned_data['login']
            
            if Utilisateur.objects.filter(email=email).exists():
                form.add_error('email', 'Cet e-mail est déjà utilisé.')
            elif Utilisateur.objects.filter(numero_telephone=numero_telephone).exists():
                form.add_error('numero_telephone', 'Ce numéro de téléphone est déjà utilisé.')
            elif Utilisateur.objects.filter(login=login).exists():
                form.add_error('login', 'Ce login est déjà utilisé.')
            else:
                form.save()
                messages.success(request, 'Inscription réussie !')
                return redirect('connexion')
        else:
            messages.error(request, 'Il y a des erreurs dans le formulaire. Veuillez corriger les erreurs et réessayer.')
    else:
        form = InscriptionForm()
    return render(request, 'v_form_inscription.html', {'form': form})













def deconnexion_view(request):
    logout(request)
    return redirect('home_view')








def connexion_view(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        mot_de_passe = request.POST.get('mot_de_passe')
        try:
            utilisateur = Utilisateur.objects.filter(login=login, mot_de_passe=mot_de_passe)
            if utilisateur.count() == 1:
                utilisateur = utilisateur.first()
                request.session['utilisateur_id'] = utilisateur.id
                return redirect('v_accueil')
               
            elif utilisateur.count() == 0:
                messages.error(request, "Identifiants invalides. Veuillez réessayer.")
            else:
                messages.error(request, "Plusieurs utilisateurs avec les mêmes identifiants. Veuillez contacter l'administrateur.")
        except Utilisateur.DoesNotExist:
            messages.error(request, "Identifiants invalides. Veuillez réessayer.")
    return render(request, 'v_form_connexion.html')















def v_accueil(request):
    if 'utilisateur_id' in request.session:
        utilisateur_id = request.session['utilisateur_id']
        utilisateur = Utilisateur.objects.get(id=utilisateur_id)
        message_bienvenue = f'Bonjour, {utilisateur.login}!'
        return render(request, 'v_accueil.html', {'message_bienvenue': message_bienvenue})
    else:
        return redirect(reverse('connexion'))








def v_ajoutMedecin(request):
    if request.method == 'POST':
        form = InscriptionFormMedecin(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inscription réussie !')
            return redirect('v_afficheMesMedecins')
        else:
            print(form.errors)
            messages.error(request, 'Il y a des erreurs dans le formulaire. Veuillez corriger les erreurs et réessayer.')
    else:
        form = InscriptionFormMedecin()

    if 'utilisateur_id' not in request.session:
        return redirect(reverse('connexion'))

    return render(request, 'v_ajoutMedecin.html', {'form': form})

  



def v_ajoutMedicament(request):
    if request.method == 'POST':
        form = InscriptionFormMedicament(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inscription réussie !')
            return redirect('v_afficheMesMedicament')
        else:
            print(form.errors)
            messages.error(request, 'Il y a des erreurs dans le formulaire. Veuillez corriger les erreurs et réessayer.')
    else:
        form = InscriptionFormMedicament()

    if 'utilisateur_id' not in request.session:
        return redirect(reverse('connexion'))

    return render(request, 'v_ajoutMedicament.html', {'form': form})










def v_rapports(request):
    if request.method == 'POST':
        form = InscriptionFormRapportMedecin(request.POST)
        if form.is_valid():
            medecin = form.cleaned_data.get('medecin')
            if not medecin:
                messages.error(request, 'Le médecin sélectionné n\'existe pas.')
                return redirect('v_rapports')

            rapport = form.save(commit=False)
            rapport.createur = Utilisateur.objects.get(id=request.session['utilisateur_id'])
            rapport.save()

            messages.success(request, 'Inscription réussie !')
            return redirect('v_afficheMesRapports')
        else:
            print(form.errors)
            messages.error(request, 'Il y a des erreurs dans le formulaire. Veuillez corriger les erreurs et réessayer.')
    else:
        # Initialiser le formulaire avec le nom de l'utilisateur connecté pré-rempli
        utilisateur_id = request.session['utilisateur_id']
        createur = Utilisateur.objects.get(id=utilisateur_id)
        form = InscriptionFormRapportMedecin(initial={'createur': f"{createur.nom} {createur.prenom}"})  # Pré-remplir avec le nom complet de l'utilisateur

        # Désactiver le champ pour empêcher toute modification
        form.fields['createur'].widget.attrs['readonly'] = True  

    return render(request, 'v_rapports.html', {'form': form})










def v_profil(request):
    if 'utilisateur_id' in request.session:
        utilisateur_id = request.session['utilisateur_id']
        utilisateur = Utilisateur.objects.get(id=utilisateur_id)
        return render(request, 'v_profil.html', {'utilisateur': utilisateur})
    else:
        return redirect(reverse('connexion'))

 





def modifier_profil(request, utilisateur_id):
    if 'utilisateur_id' not in request.session:
        return redirect(reverse('connexion'))
    
    utilisateur = get_object_or_404(Utilisateur, id=utilisateur_id)
    
    if request.method == 'POST':
        form = InscriptionForm(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            messages.success(request, 'Les modifications ont été enregistrées avec succès.')
            return redirect(reverse('v_profil'))
    else:
        form = InscriptionForm(instance=utilisateur)
    
    return render(request, 'modifier_profil.html', {'form': form, 'rapport': utilisateur})












def modifier_medecin(request, medecin_id):
    if 'utilisateur_id' not in request.session:
        return redirect(reverse('connexion'))
    
    medecin = get_object_or_404(Medecin, id=medecin_id)
    
    if request.method == 'POST':
        form = InscriptionFormMedecin(request.POST, instance=medecin)
        if form.is_valid():
            form.save()
            messages.success(request, 'Les modifications ont été enregistrées avec succès.')
            return redirect(reverse('v_afficheMesMedecins'))
    else:
        form = InscriptionFormMedecin(instance=medecin)
    
    return render(request, 'modifier_medecin.html', {'form': form, 'rapport': medecin})

            


def modifier_medicament(request, medicament_id):
    if 'utilisateur_id' not in request.session:
        return redirect(reverse('connexion'))
    
    medicament = get_object_or_404(Medicament, id=medicament_id)
    
    if request.method == 'POST':
        form = InscriptionFormMedicament(request.POST, instance=medicament)
        if form.is_valid():
            form.save()
            messages.success(request, 'Les modifications ont été enregistrées avec succès.')
            return redirect(reverse('v_afficheMesMedicament'))
    else:
        form = InscriptionFormMedicament(instance=medicament)
    
    return render(request, 'modifier_medicament.html', {'form': form, 'rapport': medicament})



def modifier_rapport(request, rapport_id):
    if 'utilisateur_id' not in request.session:
        return redirect(reverse('connexion'))
    
    rapport = get_object_or_404(Rapport, id=rapport_id)
    
    if rapport.createur.id != request.session['utilisateur_id']:
        messages.error(request, "Vous n'êtes pas autorisé à modifier ce rapport.")
        return redirect(reverse('v_afficheMesRapports'))
    
    if request.method == 'POST':
        form = InscriptionFormRapport(request.POST, instance=rapport)
        if form.is_valid():
            form.save()
            messages.success(request, 'Les modifications ont été enregistrées avec succès.')
            return redirect(reverse('v_afficheMesRapports'))
    else:
        form = InscriptionFormRapport(instance=rapport)
    
    return render(request, 'modifier_rapport.html', {'form': form, 'rapport': rapport})









def supprimer_profil(request, utilisateur_id):
    if 'utilisateur_id' not in request.session:
        return redirect(reverse('connexion'))
    utilisateur = get_object_or_404(Utilisateur, id=utilisateur_id)
    utilisateur.delete()
    messages.success(request, "Le rapport a été supprimé avec succès.")
    return redirect(reverse('home_view'))








def supprimer_rapport(request, rapport_id):
    if 'utilisateur_id' not in request.session:
        return redirect(reverse('connexion'))
    rapport = get_object_or_404(Rapport, id=rapport_id)
    if rapport.createur.id != request.session['utilisateur_id']:
        messages.error(request, "Vous n'êtes pas autorisé à supprimer ce rapport.")
        return redirect(reverse('v_afficheMesRapports'))
    rapport.delete()
    messages.success(request, "Le rapport a été supprimé avec succès.")
    return redirect(reverse('v_afficheMesRapports'))









def supprimer_medecin(request, medecin_id):
    if 'utilisateur_id' not in request.session:
        return redirect(reverse('connexion'))
    medecin = get_object_or_404(Medecin, id=medecin_id)

    medecin.delete()
    messages.success(request, "Le rapport a été supprimé avec succès.")
    return redirect(reverse('v_afficheMesMedecins'))






def supprimer_medicament(request, medicament_id):
    if 'utilisateur_id' not in request.session:
        return redirect(reverse('connexion'))
    medicament = get_object_or_404(Medicament, id=medicament_id)

    medicament.delete()
    messages.success(request, "Le medicament a été supprimé avec succès.")
    return redirect(reverse('v_afficheMesMedicament'))














def v_affiche_mes_medecins(request):
    if 'utilisateur_id' not in request.session:
        return redirect(reverse('connexion'))
    
    medecins = Medecin.objects.all()  # Récupérer tous les médecins
    return render(request, 'v_afficheMesMedecins.html', {'medecins': medecins})



def v_affiche_mes_rapports(request):
    if 'utilisateur_id' not in request.session:
        return redirect(reverse('connexion'))
    utilisateur_id = request.session['utilisateur_id']
    utilisateur = Utilisateur.objects.get(id=utilisateur_id)
    
    rapports_utilisateur = Rapport.objects.filter(createur=utilisateur)
    return render(request, 'v_afficheMesRapports.html', {'rapports_utilisateur': rapports_utilisateur})





def v_affiche_mes_medicaments(request):
    if 'utilisateur_id' not in request.session:
        return redirect(reverse('connexion'))
    
    medicaments = Medicament.objects.all()  # Récupérer tous les médecins
    return render(request, 'v_afficheMesMedicament.html', {'medicaments': medicaments})













def rapport_search(request):
    if request.method == 'GET':
        form = RapportSearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            # Convertir la chaîne de recherche en objet de date si possible
            try:
                search_date = datetime.strptime(search_query, '%Y-%m-%d').date()
                # Rechercher dans les rapports selon la date en convertissant le champ date en format date
                rapports = Rapport.objects.annotate(date_as_date=Cast('date', DateField())).filter(date_as_date=search_date)
            except ValueError:
                # Gérer une recherche invalide de date
                rapports = Rapport.objects.none()
            return render(request, 'rapport_search.html', {'form': form, 'rapports': rapports})
    else:
        form = RapportSearchForm()
    return render(request, 'rapport_search.html', {'form': form})

    



def medecin_search(request):
    if request.method == 'GET':
        form = MedecinSearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            # Filtrer les médecins par leur nom
            medecins = Medecin.objects.filter(nom__icontains=search_query)
            return render(request, 'medecin_search.html', {'form': form, 'medecins': medecins})
    else:
        form = MedecinSearchForm()
    return render(request, 'medecin_search.html', {'form': form})



