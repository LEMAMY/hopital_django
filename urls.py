# patients/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('fiche/', views.fiche_patient, name='fiche_patient'),
]
# patients/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('fiche/', views.fiche_patient, name='fiche_patient'),
    path('services/', views.services, name='services'),  # 👈 nouvelle URL
    path('reservation/', views.reservation, name='reservation'),
    path('contact/', views.contact, name='contact'),

]


