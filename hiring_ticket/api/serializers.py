from rest_framework import serializers
from hiring_ticket.models import vendor, hiring_ticket

class vendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendor
        fields = [
        'first_name',
        'last_name',
        'address', 
        'city', 
        'state',
        'zip_code',
        'phone1',
        'phone2'
        ]
    def validate_content(self, value):
        if len(value) > 10000:
            raise serializers.ValidationError("This is too long.")
            return value

class hiring_ticketSerializer:
    class Meta:
        model = hiring_ticket
        fields = [
           'ticketid',
           'equipmentid',
           'incidentid',
           'vendorid',
           'use_date',
           'start_time',
           'end_time',
           'comments',
           'repsign',
           'vendorsign',


        ]