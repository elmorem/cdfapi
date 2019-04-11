from django.contrib import admin


from .models import hiring_ticket, vendor, orderingoffice, fireincident, equipment, eeraagreement


admin.site.register(vendor)
admin.site.register(orderingoffice)
admin.site.register(fireincident)
admin.site.register(equipment)
admin.site.register(eeraagreement)
admin.site.register(hiring_ticket)