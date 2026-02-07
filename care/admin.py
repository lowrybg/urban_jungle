from django.contrib import admin
from care.models import CareTip


@admin.register(CareTip)
class CareTipAdmin(admin.ModelAdmin):
    list_display = ('title',)
