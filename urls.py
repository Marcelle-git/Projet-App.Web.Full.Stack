from django.urls import path
# from . import APIviews
from . import views

urlpatterns = [
    path('', views.products)
    # path('', APIviews.getProducts),
]


urlpatterns = [
    path('', views.clients)
    # path('', APIviews.getClients),
]


urlpatterns = [
    path('', views.credits_par_client)
    # path('', APIviews.getCredits_par_clients),
]
