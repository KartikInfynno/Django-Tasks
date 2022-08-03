from django.db import models
from Auths.models import My_User


category = (
    ('Shoes', 'Shoes'),
    ('Jacket', 'Jacket'),
    ('Shirt', 'Shirt'),
    ('T-shirt', 'T-shirt'),
    ('Bag', 'Bag'),
    ('Glasses', 'Glasses'),
    ('Others', 'Others'),
)

class Add_Product(models.Model):
    user = models.ForeignKey(My_User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'products')
    price = models.FloatField()
    category = models.CharField(max_length=255,choices = category)

    def __str__(self):
        return f"Product : {self.name} , User: {self.user.username}"
