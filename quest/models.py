from django.db import models

class Quest(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Полное имя")
    birthday = models.DateField(verbose_name="Дата рождения")
    idgender = models.ForeignKey('gender.Gender', on_delete = models.CASCADE, verbose_name="Номер пола")
    idstatus = models.ForeignKey('status.Status', on_delete = models.CASCADE, verbose_name="Номер статуса")

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['birthday']
