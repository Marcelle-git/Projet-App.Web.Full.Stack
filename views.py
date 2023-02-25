# from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader

def products(request):
    return HttpResponse('Liste des produits') 


def clients(request):
    return HttpResponse('Liste des clients') 


def credits_par_client(request):
    return HttpResponse('Liste des credits_par_client')            
    
    
