from django.db import models

class Room(models.Model):
    Number = models.PositiveBigIntegerField(verbose_name="Номер")
    RoomTypeId = models.ForeignKey('roomtype.RoomType', on_delete=models.CASCADE, verbose_name="Номер типа комнаты")
    HotelId = models.ForeignKey('hotel.Hotel', on_delete=models.CASCADE, verbose_name="Номер отеля")

    def __str__(self):
        return str(self.Number)

    class Meta:
        ordering = ['Number']
