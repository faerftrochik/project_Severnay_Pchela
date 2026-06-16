from django.db import models

class RoomType(models.Model):
    RoomTypeName = models.CharField(max_length=200, verbose_name="Тип комнаты")

    def __str__(self):
        return self.RoomTypeName
