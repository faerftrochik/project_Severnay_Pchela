from django.db import models

class Guest(models.Model):
    FullName = models.CharField(max_length=100, verbose_name="Полное имя")
    Birthday = models.DateField(verbose_name="Дата рождения")
    GenderId = models.ForeignKey('gender.Gender', on_delete = models.CASCADE, verbose_name="Номер пола")
    StatusId = models.ForeignKey('status.Status', on_delete = models.CASCADE, verbose_name="Номер статуса")

    def __str__(self):
        return self.FullName

    class Meta:
        ordering = ['Birthday']
