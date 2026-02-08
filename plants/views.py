from django.views.generic import ListView
from .models import Plant

class PlantListView(ListView):
    model = Plant
    template_name = 'plants/catalog.html'
    context_object_name = 'plants'