from django.urls import path
from .views import PlantListView, PlantCreateView

urlpatterns = [
    path('catalog/', PlantListView.as_view(), name='catalog'),
    path('create/', PlantCreateView.as_view(), name='create_plant'),
]