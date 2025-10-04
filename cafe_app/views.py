
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import MailSender, Partner


def index(request):
    return render(request, 'index.html')



def success_reserv(request):
    if request.method == 'POST':
        entrepreneur = True if request.POST.get('entrepreneur', '') == 'Oui' else False
        nom = request.POST.get('nom', '')
        email = request.POST.get('email', '')
        adresse = request.POST.get('adresse', '')
        about = request.POST.get('about', '')
        secteur = request.POST.get('secteur', '')
        motivation = request.POST.get('motivation', '')
        partenaire = request.POST.get('partenaire', '')

        sujet = "Café des Entrepreneurs"
        message = f"""
            Une réservation de {nom}, pour l'evenement du café des entrepreneurs !
            
            RÉSERVATION REÇUE
            Entrepreneur : {"Oui" if entrepreneur else "Non"}
            Nom : {nom}
            Email : {email}
            Adresse : {adresse}
            Secteur : {secteur}
            Poste ou fonction : {about}
            Motivation : {motivation}
            Partenaire ou sponsor : {partenaire}

        Cette information est adressé au commité organisateur.
        """
        mails = MailSender.objects.all()
        for mail in mails:
            send_mail(
            sujet,
            message,
            'kenaskili@gmail.com',  # From
            [f"{mail.email}"],  # To
            fail_silently=False,
        )
        try:
            res = Partner.objects.get(email=email)
            if res:
                res.entrepreneur=entrepreneur
                res.name=nom
                res.Address=adresse
                res.about = about
                res.activity_section=secteur
                res.why=motivation
                res.partner_or_sponsor=partenaire
                res.save()
                return render(request, "success.html", {
                "nom": nom,
                "secteur": secteur,
            })
        except:
            Partner.objects.create(
                entrepreneur=entrepreneur,
                name=nom,
                email=email,
                Address=adresse,
                about = about,
                activity_section=secteur,
                why=motivation,
                partner_or_sponsor=partenaire)
        finally:
            return render(request, "success.html", {
                "nom": nom,
                "secteur": secteur,
            })
    return render(request, 'succes.html')


