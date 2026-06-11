from django.db import models

class Roomtype(models.Model):
    room_name = models.CharField(max_length=200, verbose_name="Тип комнаты")

    def __str__(self):
        return self.room_name
