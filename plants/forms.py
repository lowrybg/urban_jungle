from django import forms
from django.core.exceptions import ValidationError
from .models import Plant, Room

class PlantCreateForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'species', 'height_cm', 'water_needs_ml', 'room', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g., Ficus elastica'}),
        }

    def clean_water_needs_ml(self):
        water = self.cleaned_data.get('water_needs_ml')
        if water is not None and water > 5000:
            raise ValidationError("Water needs cannot exceed 5000ml per week.")
        return water

class PlantUpdateForm(forms.ModelForm):
    class Meta:
        model = Plant
        exclude = ['species', 'photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['name'].help_text = "The plant's name can not be changed once created."


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'light_level']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g., Living Room'}),
        }
