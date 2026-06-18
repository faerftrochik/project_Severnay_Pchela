from django.db import models

class History(models.Model):
    GuestId = models.ForeignKey('guest.Guest', on_delete=models.CASCADE, verbose_name="Номер гостя")
    RoomId = models.ForeignKey('room.Room', on_delete=models.CASCADE, verbose_name="Номер комнаты")
    CheckIn = models.DateField(verbose_name="Заселился")
    CheckOut = models.DateField(verbose_name="Выселился")
    Comment = models.CharField(max_length=500, verbose_name="Комментарий")

    def __str__(self):
        return str(self.Comment)

    class Meta:
        ordering = ['Comment']