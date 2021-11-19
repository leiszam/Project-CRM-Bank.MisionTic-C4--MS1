from rest_framework import serializers
from .models import  soporte, PQR


class soporteSerializer(serializers.ModelSerializer):
    class Meta: 
       model = soporte
       fields ='__all__'
    

class PQRSerializer(serializers.ModelSerializer):
    soport_id = soporteSerializer()

    class Meta: 
       model = PQR
       fields = ['id','soport_id','tipo', 'info','created']