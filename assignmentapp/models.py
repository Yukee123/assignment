from django.db import models

# Create your models here.
class Types_Of_Games(models.Model):
    name = models.CharField(max_length=30)
    releasedate = models.CharField(max_length=30)
    type = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Types_Of_Games"
        verbose_name_plural = "Types_Of_Gamess"

    def __str__(self):
        return self.name