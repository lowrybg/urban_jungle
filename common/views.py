from django.shortcuts import render
from django.views.generic import TemplateView
from plants.models import Plant, Room
class HomeView(TemplateView):
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_plants'] = Plant.objects.count()
        context['total_rooms'] = Room.objects.count()
        return context

def custom_404(request, exception):
    return render(request, 'common/404.html', status=404)