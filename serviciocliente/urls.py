from django.urls import path
from .views import soporteListCreate, soporteUpdateDelete,PQRListCreate,PQRUpdateDelete

urlpatterns = [

    path('soporte/', soporteListCreate.as_view()),
    path('soporte/<pk>',soporteUpdateDelete.as_view()),
    path('PQR/', PQRListCreate.as_view()),
    path('PQR/<pk>',PQRUpdateDelete.as_view())

]