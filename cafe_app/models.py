from django.db import models


class Partner(models.Model):
    entrepreneur = models.BooleanField(null=True, default=False, verbose_name="Si entrepreneur")
    name = models.CharField(max_length=255, verbose_name="Nom")
    email = models.EmailField(unique=True, primary_key=True, verbose_name="email")
    Address = models.CharField(max_length=1000, verbose_name="adresse")
    about = models.CharField(max_length=300,default="", verbose_name="Poste en entreprise ou fonction metier")
    activity_section = models.CharField(max_length=500, verbose_name="Secteur d'activités")
    why = models.CharField(max_length=255, verbose_name="(Motivation)Raison de participation")
    partner_or_sponsor = models.CharField(max_length=10, verbose_name="Sponsor ou partenaire")
    
    class Meta:
        ordering = ['-pk']

class MailSender(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self): return self.name
