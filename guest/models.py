from django.db import models
from django.urls import reverse

class Guest(models.Model):
    FullName = models.CharField(max_length=100, verbose_name="Полное имя")
    Birthday = models.DateField(verbose_name="Дата рождения")
    GenderId = models.ForeignKey('gender.Gender', on_delete = models.CASCADE, verbose_name="Номер пола")
    StatusId = models.ForeignKey('status.Status', on_delete = models.CASCADE, verbose_name="Номер статуса")

    def get_update_url(self):
        return reverse("guest_update", kwargs={"pk": self.pk})

    def __str__(self):
        return self.FullName

    class Meta:
        ordering = ['Birthday']
