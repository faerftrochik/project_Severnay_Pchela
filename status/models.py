from django.db import models

class Status(models.Model):
    StatusName = models.CharField(max_length=100, verbose_name="Статус")

    def __str__(self):
        return self.StatusName

