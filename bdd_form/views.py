from django.shortcuts import render
import logging
from .models import Commune, Client, Voiture, Technicien, Reparation, Piece_detachee
from .forms import ClientForm, VoitureForm,ReparationForm
from django.utils.dateparse import parse_date,parse_duration
# Create your views here.

logger = logging.getLogger(__name__)

def dashboard(request):

    communes = Commune.objects.all()
    voitures = Voiture.objects.all()
    clients = Client.objects.all()
    techniciens = Technicien.objects.all()
    pieces = Piece_detachee.objects.all()
    reparations = Reparation.objects.all()

    clientform = ClientForm()
    voitureform = VoitureForm()
    reparationform = ReparationForm()

    loading_status = "get"
    tab_load='client_voiture'

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
                immatriculation = request.POST.get('immatriculation').replace("-", "")
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
        
        if 'ajout_reparation' in request.POST:

            tab_load='client_voiture'

            voiture_id = request.POST.get('voiture_id')
            technicien_id = request.POST.get('technicien_id')
            pieces_id = request.POST.getlist('piece_detachee')
            date_reparation = parse_date(request.POST.get('date'))
            duree = parse_duration(request.POST.get('duree')+':00')

            if request.POST.get('forfaitaire') == 'on':
                prix = request.POST.get('prix')
            else:
                prix= duree.seconds/3600*50


   
            reparation = Reparation.objects.create(
                technicien = Technicien.objects.get(id=technicien_id),
                remarque_technicien = request.POST.get('remarque'),
                voiture = Voiture.objects.get(id=voiture_id),
                date = date_reparation,
                duree = duree,
                nom = request.POST.get('nom'),
                prix = prix,
            )
            for id in pieces_id:
                reparation.pieces_detachees.add(id)
            
            tab_load='reparation'

        

        if 'suppr_client' in request.POST:
            id_client_suppr = request.POST.get('suppr_client')
            client_suppr = Client.objects.get(id=id_client_suppr)
            client_suppr.delete()

        if 'suppr_voiture' in request.POST:
            id_voiture_suppr = request.POST.get('suppr_voiture')
            voiture_suppr = Voiture.objects.get(id=id_voiture_suppr)
            voiture_suppr.delete()
        
        if 'modif_remarque' in request.POST:
            id_rep_modif = request.POST.get('reparation_id')
            remarque = request.POST.get('remarque')
            print(remarque)
           
            rep_modif = Reparation.objects.get(id=id_rep_modif)
            print(rep_modif)
            rep_modif.remarque_technicien = remarque
            rep_modif.save()

            tab_load='reparation'


    context = {
        'communes': communes,
        'voitures': voitures,
        'clients': clients,
        'techniciens': techniciens,
        'pieces': pieces,
        'reparations': reparations,
        'clientform': clientform,
        'voitureform': voitureform,
        'reparationform': reparationform,
        'loading_status': loading_status,
        'tab_load': tab_load,
    }

    return render(request, 'bdd_form/dashboard.html', context)
