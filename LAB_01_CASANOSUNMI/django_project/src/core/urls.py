from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('api/items/', views.api_items, name='api_items'),
    path('api/add/', views.api_add_item, name='api_add_item'),
]
