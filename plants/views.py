from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import get_object_or_404

from .forms import PlantCreateForm, PlantUpdateForm, RoomForm
from .models import Plant, Room

class PlantListView(ListView):
    model = Plant
    template_name = 'plants/catalog.html'
    context_object_name = 'plants'

class PlantCreateView(CreateView):
    model = Plant
    form_class = PlantCreateForm
    template_name = 'plants/create_plant.html'
    success_url = reverse_lazy('catalog')

class PlantUpdateView(UpdateView):
    model = Plant
    form_class = PlantUpdateForm
    template_name = 'plants/edit_plant.html'
    success_url = reverse_lazy('catalog')

class PlantDeleteView(DeleteView):
    model = Plant
    template_name = 'plants/delete_plant.html'
    success_url = reverse_lazy('catalog')

class PlantDetailView(DetailView):
    model = Plant
    template_name = 'plants/detail_plant.html'
    context_object_name = 'plant'


class RoomListView(ListView):
    model = Room
    template_name = 'plants/room_list.html'
    context_object_name = 'rooms'



class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'plants/create_room.html'
    success_url = reverse_lazy('room_list')

class RoomUpdateView(UpdateView):
    model = Room
    form_class = RoomForm
    template_name = 'plants/edit_room.html'
    success_url = reverse_lazy('room_list')

class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'plants/delete_room.html'
    success_url = reverse_lazy('room_list')

class PlantByRoomListView(ListView):
    model = Plant
    template_name = 'plants/plants_by_room.html'
    context_object_name = 'plants'


    def get_queryset(self):
        return Plant.objects.filter(room_id=self.kwargs['room_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room'] = get_object_or_404(Room, pk=self.kwargs['room_id'])
        return context

