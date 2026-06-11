from django.db import models

class Gender(models.Model):
    gender_name = models.CharField(max_length=50, verbose_name="Имя пола")

    def __str__(self):
        return self.gender_name
