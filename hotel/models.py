from django.db import models

class Hotel(models.Model):
    HotelName = models.CharField(max_length=100, verbose_name="Имя отеля")

    def __str__(self):
        return self.HotelName
