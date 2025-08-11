# patients/views.py
from django.shortcuts import render

def accueil(request):
    return render(request, 'patients/accueil.html')

def fiche_patient(request):
    return render(request, 'patients/fiche.html')
def services(request):
    specialites = [
        "Cardiologie",
        "Neurologie",
        "Orthopédie",
        "Ophtalmologie",
        "Pédiatrie",
        "Gynécologie",
        "Dermatologie"
    ]
    return render(request, 'patients/services.html', {'specialites': specialites})

from django.shortcuts import render
from django.utils import timezone

def reservation(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        specialite = request.POST.get('specialite')
        date = request.POST.get('date')
        heure = request.POST.get('heure')
        contact = request.POST.get('contact')

        # 👉 Ici tu pourrais enregistrer les données dans la base
        message = f"Rendez-vous réservé pour {prenom} {nom} le {date} à {heure} en {specialite}."
        return render(request, 'patients/reservation.html', {'message': message})

    return render(request, 'patients/reservation.html')

def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        sujet = request.POST.get('sujet')
        message = request.POST.get('message')

        confirmation = f"Merci {nom}, votre message a bien été envoyé."
        return render(request, 'patients/contact.html', {'confirmation': confirmation})

    return render(request, 'patients/contact.html')

   

