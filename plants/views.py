from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import PlantForm
from .models import Plant

class PlantListView(ListView):
    model = Plant
    template_name = 'plants/catalog.html'
    context_object_name = 'plants'

class PlantCreateView(CreateView):
    model = Plant
    form_class = PlantForm
    template_name = 'plants/create_plant.html'
    success_url = reverse_lazy('catalog')


class PlantUpdateView(UpdateView):
    model = Plant
    form_class = PlantForm
    template_name = 'plants/edit_plant.html'
    success_url = reverse_lazy('catalog')

class PlantDeleteView(DeleteView):
    model = Plant
    template_name = 'plants/delete_plant.html'
    success_url = reverse_lazy('catalog')
