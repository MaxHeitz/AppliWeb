from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    path('', views.accueil, name='accueil'),
    path('article/<int:id>-<slug:slug>$', views.lire, name='lire'),
    path('contact/', views.contact, name='contact')

]
