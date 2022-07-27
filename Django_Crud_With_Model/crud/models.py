from django.db import models

class Crud(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.number}"
