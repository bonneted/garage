from django.db import models

class Commune(models.Model):
    nom = models.CharField(max_length=100)
    nb_client = models.IntegerField()

class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    nom_admin = models.CharField(max_length=100)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

class Voiture(models.Model):
    immatriculation = models.CharField(max_length=7)
    kilometrage = models.IntegerField(default=0)
    marque = models.CharField(max_length=100)
    type_voiture = models.CharField(max_length=100)
    date_arrivee = models.DateField(auto_now_add=True)
    proprietaire = models.ForeignKey(Client, on_delete=models.CASCADE)

class Piece_detachee(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

class Technicien(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

class Reparation(models.Model):
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    remarque_technicien = models.TextField()
    nom = models.CharField(max_length=100,blank=True)
    duree = models.DurationField(blank=True)
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)
    pieces_detachees= models.ManyToManyField(Piece_detachee,related_name='reparations')
    
