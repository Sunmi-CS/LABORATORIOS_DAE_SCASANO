from django.urls import path
from .views import lista_candidatos

urlpatterns = [
    path('candidatos/', lista_candidatos),
]

