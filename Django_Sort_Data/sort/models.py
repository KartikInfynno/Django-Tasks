from django.db import models


class Sort(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    dob = models.DateField()

    def __str__(self):
        return self.name
