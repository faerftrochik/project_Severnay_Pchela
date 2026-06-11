from django.db import models

class History(models.Model):
    idquest = models.ForeignKey('quest.Quest', on_delete=models.CASCADE, verbose_name="Номер квеста")
    idroom = models.ForeignKey('room.Room', on_delete=models.CASCADE, verbose_name="Номер комнаты")
    checkin = models.DateField(verbose_name="Заселился")
    checkOut = models.DateField(verbose_name="Выселился")
    comment = models.CharField(max_length=500, verbose_name="Комментарий")

    def __str__(self):
        return str(self.comment)

    class Meta:
        ordering = ['comment']