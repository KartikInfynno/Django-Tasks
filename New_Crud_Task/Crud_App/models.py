from random import choices
from django.db import models



choices = (
    ('Male' , "Male"),
    ('Female' , "Female"),
    ('Other' , "Other"),
)

class Crud(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    contact_no = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length = 20 ,choices = choices)

    def __str__(self):
        return self.first_name
