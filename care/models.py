from django.db import models

from plants.models import Plant


class CareTip(models.Model):
    title = models.CharField(max_length=150)
    instructions = models.TextField()

    #One Tip -> Many Plants
    related_plants = models.ManyToManyField(
    Plant,
    related_name='care_tips',
        blank=True,

    )

    def __str__(self):
        return self.title