from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class soporte (models.Model, ):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64,null=True, blank=True)
    phone = models.PositiveIntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    photo = models.FileField (null=True, blank=True)
    is_active = models.BooleanField(default=True)


class PQR(models.Model):
    id = models.AutoField(primary_key=True)
    soport_id = models.ForeignKey(soporte,on_delete=SET_NULL, null=True)
    tipo =CharField(max_length=64)
    info= models.TextField()
    created = models.DateField()
