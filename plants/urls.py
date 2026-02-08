from django.urls import path
from .views import PlantListView

urlpatterns = [
    path('catalog/', PlantListView.as_view(), name='catalog'),
]