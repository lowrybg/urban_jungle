from django.urls import path
from .views import PlantListView, PlantCreateView, PlantUpdateView, PlantDeleteView, PlantDetailView, RoomListView, \
RoomCreateView, RoomUpdateView, RoomDeleteView

urlpatterns = [
    path('catalog/', PlantListView.as_view(), name='catalog'),
    path('create/', PlantCreateView.as_view(), name='create_plant'),
    path('edit/<int:pk>/', PlantUpdateView.as_view(), name='edit_plant'),
    path('delete/<int:pk>/', PlantDeleteView.as_view(), name='delete_plant'),
    path('plant/<int:pk>/', PlantDetailView.as_view(), name='detail_plant'),


    path('rooms/', RoomListView.as_view(), name='room_list'),
    path('rooms/create/', RoomCreateView.as_view(), name='create_room'),
    path('rooms/edit/<int:pk>/', RoomUpdateView.as_view(), name='edit_room'),
    path('rooms/delete/<int:pk>/', RoomDeleteView.as_view(), name='delete_room'),
]
