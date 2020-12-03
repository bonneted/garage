from django.shortcuts import render

from .models import Commune, Client, Voiture, Technicien, Reparation, Piece_detachee
from .forms import ClientForm, VoitureForm
# Create your views here.


def index(request):

    communes = Commune.objects.all()
    context = {
        'communes': communes
    }

    return render(request, 'bdd_form/search_form.html',context)

def search(request):

    communes = Commune.objects.all()

    context = {
        'communes': communes
    }

    if request.method == 'POST':

        if 'ajout_commune' in request.POST:
            nom_commune = request.POST.get('nom_commune')
            commune = Commune.objects.filter(nom=nom_commune)
            if not commune.exists():
                Commune.objects.create(
                    nom=nom_commune,
                    nb_client=0
                )

        if 'ajout_client' in request.POST:
            nom_commune = request.POST.get('commune_client')
            commune = Commune.objects.get(nom=nom_commune)
            commune.nb_client += 1
            commune.save()

        if 'suppression_commune' in request.POST:
            nom_commune = request.POST.get('commune_suppr')
            commune = Commune.objects.get(nom=nom_commune)
            commune.delete()
            # commune.save()

    return render(request, 'bdd_form/dashboard.html', context)


def dashboard(request):

    communes = Commune.objects.all()
    voitures = Voiture.objects.all()
    clients = Client.objects.all()
    clientform = ClientForm()
    voitureform = VoitureForm()

    loading_status = "get"

    if request.method == 'POST':

        if 'ajout_client' in request.POST:
            clientform = ClientForm(request.POST)

            if clientform.is_valid():
                nom = request.POST.get('nom')
                prenom = request.POST.get('prenom')
                nom_admin = request.POST.get('nom_admin')
                nom_commune = request.POST.get('commune')

                client = Client.objects.filter(nom=nom,prenom=prenom)
                if not client.exists():
                    commune = Commune.objects.filter(nom=nom_commune)

                    if not commune.exists():
                        commune = Commune.objects.create(nom=nom_commune,nb_client=1)
                        commune.save()
                    else:
                        commune = Commune.objects.get(nom=nom_commune)
                        commune.nb_client += 1
                        commune.save()

                    client = Client.objects.create(
                        nom = nom,
                        prenom = prenom,
                        nom_admin = nom_admin,
                        commune = commune
                    )

                    loading_status='client_success'
                else:
                    loading_status='client_fail'

        if 'ajout_voiture' in request.POST:
            voitureform = VoitureForm(request.POST)

            if voitureform.is_valid():
                request_post = request.POST
                immatriculation = request.POST.get('immatriculation').replace("-", "")
                marque = request.POST.get('marque')
                voiture = Voiture.objects.filter(immatriculation=immatriculation)
                proprietaire_id = request.POST.get('proprietaire')
                if not voiture.exists():
                    voiture = Voiture.objects.create(
                        immatriculation=immatriculation,
                        marque = request.POST.get('marque'),
                        type_voiture = request.POST.get('type_voiture'),
                        kilometrage = request.POST.get('kilometrage'),
                        proprietaire = Client.objects.get(id=proprietaire_id)
                    )
                    loading_status='voiture_success'
                else:
                    loading_status='voiture_fail'

        if 'suppr_client' in request.POST:
            id_client_suppr = request.POST.get('suppr_client')
            client_suppr = Client.objects.get(id=id_client_suppr)
            client_suppr.delete()

        if 'suppr_voiture' in request.POST:
            id_voiture_suppr = request.POST.get('suppr_voiture')
            voiture_suppr = Voiture.objects.get(id=id_voiture_suppr)
            voiture_suppr.delete()


    context = {
        'communes': communes,
        'voitures': voitures,
        'clients': clients,
        'clientform': clientform,
        'voitureform': voitureform,
        'loading_status': loading_status,
    }

    return render(request, 'bdd_form/dashboard.html', context)
