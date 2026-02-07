from django.contrib import admin
from .models import Room, Plant

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'light_level')

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'room', 'height_cm')
    list_filter = ('room',)

