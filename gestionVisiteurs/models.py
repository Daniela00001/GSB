from django.db import models

class Utilisateur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    complement_adresse = models.CharField(max_length=255, blank=True, null=True)
    ville = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    numero_telephone = models.CharField(max_length=20)
    date_embauche = models.DateField()
    login = models.CharField(max_length=50)
    mot_de_passe = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Medecin(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    numero_telephone = models.CharField(max_length=20)
    specialisteComplimentaire = models.CharField(max_length=255, blank=True, null=True)
    departement = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Medicament(models.Model):
    id = models.AutoField(primary_key=True)
    nomCommercial = models.CharField(max_length=100)
    composition = models.CharField(max_length=255, blank=True, null=True)
    effets = models.CharField(max_length=100)
    contreIndications = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nomCommercial
    

class Rapport(models.Model):
    date = models.CharField(max_length=100)
    motif = models.CharField(max_length=100)
    bilan = models.CharField(max_length=100)
    createur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)
    medecin = models.ForeignKey(Medecin, on_delete=models.SET_NULL, null=True)
    medicament = models.ForeignKey(Medicament, on_delete=models.SET_NULL, null=True)
    quantite = models.CharField(max_length=100, default='0')
