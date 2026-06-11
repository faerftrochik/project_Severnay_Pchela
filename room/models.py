from django.db import models

class Room(models.Model):
    nomber = models.PositiveBigIntegerField(verbose_name="Номер")
    idroomtype = models.ForeignKey('roomtype.Roomtype', on_delete=models.CASCADE, verbose_name="Номер типа комнаты")
    idhotel = models.ForeignKey('hotel.Hotel', on_delete=models.CASCADE, verbose_name="Номер отеля")

    def __str__(self):
        return str(self.nomber)

    class Meta:
        ordering = ['nomber']
