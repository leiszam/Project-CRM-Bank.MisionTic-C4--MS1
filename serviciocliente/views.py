from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from .serializer import soporteSerializer, PQRSerializer
from .models import soporte, PQR

# Create your views here.

class soporteListCreate(generics.ListCreateAPIView):
    queryset = soporte.objects.all()
    serializer_class = soporteSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class soporteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = soporte.objects.all()
    serializer_class = soporteSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class PQRListCreate(generics.ListCreateAPIView):
    queryset = PQR.objects.all()
    serializer_class = PQRSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class PQRUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PQR.objects.all()
    serializer_class = PQRSerializer