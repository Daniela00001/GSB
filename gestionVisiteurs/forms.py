from django import forms
from .models import Utilisateur, Rapport, Medecin, Medicament
from django.contrib.auth.forms import AuthenticationForm
import re


class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    
    def clean_numero_telephone(self):
        numero_telephone = self.cleaned_data['numero_telephone']
        # Expression régulière pour vérifier le format du numéro de téléphone français
        if not re.match(r'^0[1-9]([-. ]?[0-9]{2}){4}$', numero_telephone):
            raise forms.ValidationError("Le numéro de téléphone doit être au format français.")
        return numero_telephone


class InscriptionFormRapport(forms.ModelForm):
    class Meta:
        model = Rapport
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


class InscriptionFormMedecin(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    def clean_numero_telephone(self):
        numero_telephone = self.cleaned_data['numero_telephone']
        # Expression régulière pour vérifier le format du numéro de téléphone français
        if not re.match(r'^0[1-9]([-. ]?[0-9]{2}){4}$', numero_telephone):
            raise forms.ValidationError("Le numéro de téléphone doit être au format français.")
        return numero_telephone


class InscriptionFormMedicament(forms.ModelForm):
    class Meta:
        model = Medicament
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


class ConnexionForm(AuthenticationForm):
    username = forms.CharField(label="Login", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class InscriptionFormRapportMedecin(forms.ModelForm):
    date = forms.CharField(max_length=100)
    motif = forms.CharField(max_length=100)
    bilan = forms.CharField(max_length=100)
    quantite = forms.CharField(max_length=100)
    medecin = forms.ModelChoiceField(queryset=Medecin.objects.all())
    medicament = forms.ModelChoiceField(queryset=Medicament.objects.all(), empty_label=None)  # Supprimer le champ de saisie pour le médicament

    class Meta:
        model = Rapport
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def save(self, commit=True):
        rapport = super().save(commit=False)
        rapport.medecin = self.cleaned_data['medecin']
        rapport.medicament = self.cleaned_data['medicament']

        if commit:
            rapport.save() 
        return rapport


class RapportSearchForm(forms.Form):
    search_query = forms.CharField(label='Rechercher')

class MedecinSearchForm(forms.Form):
    search_query = forms.CharField(label='Rechercher')
