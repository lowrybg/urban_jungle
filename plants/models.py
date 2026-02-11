from django.db import models

from plants.validators import validate_start_with_capital


class Room(models.Model):
    SUNLIGHT_CHOICES = [
        ('LOW', 'Low Light'),
        ('MED', 'Medium Light'),
        ('HIGH', 'Direct Sunlight'),
    ]
    name = models.CharField(
        max_length=100,
    )
    light_level = models.CharField(max_length=4, choices=SUNLIGHT_CHOICES)
    def __str__(self):
        return self.name

class Plant(models.Model):
    name = models.CharField(max_length=100,
                            validators=[validate_start_with_capital]
                            )
    species = models.CharField(max_length=100, blank=True)

    height_cm = models. FloatField(help_text="Height in centimeters")
    water_needs_ml = models. PositiveSmallIntegerField(help_text="Water per week in milliliters")

    room = models.ForeignKey(
        Room,
        on_delete=models.SET_NULL,
        null=True,
        related_name='plants',

    )

    photo = models.ImageField(upload_to='plants/', blank=True, null=True)

    def __str__(self):
        return self.name
