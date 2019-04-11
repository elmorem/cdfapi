from django.conf import settings
from django.db import models
import datetime 

class vendor(models.Model):
    vendorid =      models.AutoField(primary_key=True)
    first_name =    models.CharField(max_length=80)
    last_name =     models.CharField(max_length=80)
    address =       models.CharField(max_length=80)
    city =          models.CharField(max_length=80)
    state =         models.CharField(max_length=80)
    zip_code =      models.IntegerField()
    phone1 =        models.CharField(max_length=14)
    phone2 =        models.CharField(max_length=14)

    class Meta:
        db_table = 'vendor' 
        verbose_name = 'Vendor'
        verbose_name = 'Vendors'

class orderingoffice(models.Model):
    orderingofficeid =  models.AutoField(primary_key=True)
    name =              models.CharField(max_length=80)
    address =           models.CharField(max_length=80)
    city =              models.CharField(max_length=80)
    state =         models.CharField(max_length=80)
    zip_code =          models.IntegerField() 
    phone =             models.CharField(max_length=14)

    class Meta:
        db_table = 'orderingoffice'
        verbose_name = 'Ordering Office'
        verbose_name = 'Ordering Offices'



class fireincident(models.Model):
    incidentid =    models.AutoField(primary_key=True)
    incident_name = models.CharField(max_length=80)

    class Meta:
        db_table = 'fireincident'
        verbose_name = 'Fire Incident'
        verbose_name = 'Fire Incidents'



class equipment(models.Model):
    equipmentid =       models.AutoField(primary_key=True)
    vendorid =          models.ForeignKey(vendor, on_delete=models.CASCADE, default=None)
    make =              models.CharField(max_length=80)
    model =             models.CharField(max_length=80)
    serial_num =        models.IntegerField()
    license_num =       models.IntegerField()
    operator =          models.CharField(max_length=80)

    class Meta:
        db_table = 'equipment'
        verbose_name = 'Equipment'
        verbose_name = 'Equipments'

class eeraagreement(models.Model):
    eeraid =            models.AutoField(primary_key=True)
    orderingofficeid =  models.ForeignKey(orderingoffice, on_delete=models.CASCADE)
    vendorid    =       models.ForeignKey(vendor, on_delete=models.CASCADE, default=None)
    agreement_num =     models.IntegerField()
    begin_date =        models.DateField(default=datetime.date.today)
    end_date  =         models.DateField(default=datetime.date.today)

    class Meta:
        db_table = 'eeraagreement'
        verbose_name = 'Eeraagreement'
        verbose_name = 'Eeraagreements'


class hiring_ticket(models.Model):  
    ticketid =      models.AutoField(primary_key=True)
    incidentid =    models.ForeignKey(fireincident, on_delete=models.CASCADE)
    vendorid =      models.ForeignKey(vendor, on_delete=models.CASCADE, default=None)
    equipmentid =   models.ForeignKey(equipment, on_delete=models.CASCADE)
    use_date =      models.DateField(default=datetime.date.today)
    start_time =    models.DateField(default=datetime.date.today)
    end_time =      models.DateField(default=datetime.date.today)
    assignment =    models.CharField(max_length=200)
    comments =      models.CharField(max_length=200, default='comments')
    repname =       models.CharField(max_length=200, default='repname')
    repsign =       models.CharField(max_length=80, default ='signature')
    vendorsign =    models.CharField(max_length=80, default ='signature')
    sign_date =     models.DateField(default=datetime.date.today)

    class Meta:
        db_table = 'hiring_ticket'
        verbose_name = "Hiring Ticket"
        verbose_name = "Hiring Tickets"
