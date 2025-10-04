from django.contrib import admin
from .models import MailSender, Partner

# Register your models here.

class MailSenderAdmin(admin.ModelAdmin):
    model = MailSender


class ReservationAdmin(admin.ModelAdmin):
    model = Partner
    list_display = (
        'entrepreneur',
        'name',
        'about',
        'email',
        'Address',
        'activity_section',
        'why',
        'partner_or_sponsor',
    )

admin.site.register(MailSender, MailSenderAdmin)
admin.site.register(Partner, ReservationAdmin)