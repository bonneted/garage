from django import forms
from .models import Client

class ClientForm(forms.Form):
    nom = forms.CharField(
        label='Nom',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input is-small','placeholder':'ex: Sorel'}),
        required=True
        )
    prenom = forms.CharField(
        label='Prénom',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input is-small','placeholder':'ex: Julien'}),
        required=True
        )
    nom_admin = forms.CharField(
        label='Référent',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input is-small','placeholder':'ex: Rênal'}),
        required=True
        )

    commune = forms.CharField(
        label='Commune',
        widget=forms.TextInput(attrs={'class': 'input is-small','placeholder':'ex: Verrières','list':'commune_list'}),
        required=True)

class VoitureForm(forms.Form):
    marque = forms.CharField(
        label='Marque',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input is-small','placeholder':'ex: Peugeot'}),
        required=True
        )
    type_voiture = forms.CharField(
        label='Type',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input is-small','placeholder':'ex: 208'}),
        required=True
        )
    immatriculation = forms.CharField(
        label='Immatriculation',
        max_length=9,
        widget=forms.TextInput(attrs={'class': 'input is-small','placeholder':'ex: 12AAA12, 12-AAA-12'}),
        required=True
        )
    kilometrage = forms.IntegerField(
        label='Kilométrage',
        widget=forms.NumberInput(attrs={'class': 'input is-small','placeholder':'ex: 10000'}),
        required=True
        )


class ReparationForm(forms.Form):
    date = forms.DateField(
        label='Nom',
        widget=forms.TextInput(attrs={'class': 'input','type':'date'}),
        required=True
        )
    duree = forms.TimeField(
        label='Nom',
        widget=forms.TextInput(attrs={'class': 'input','type':'time'}),
        required=True
        )