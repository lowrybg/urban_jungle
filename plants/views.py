from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

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
