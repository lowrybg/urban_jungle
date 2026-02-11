from django.urls import path
from .views import PlantListView, PlantCreateView, PlantUpdateView, PlantDeleteView, PlantDetailView

urlpatterns = [
    path('catalog/', PlantListView.as_view(), name='catalog'),
    path('create/', PlantCreateView.as_view(), name='create_plant'),
    path('edit/<int:pk>/', PlantUpdateView.as_view(), name='edit_plant'),
    path('delete/<int:pk>/', PlantDeleteView.as_view(), name='delete_plant'),
    path('plant/<int:pk>/', PlantDetailView.as_view(), name='detail_plant'),
]