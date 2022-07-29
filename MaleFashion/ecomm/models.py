from django.db import models


category = (
    ('shoes', 'shoes'),
    ('jacket', 'jacket'),
    ('shirt', 'shirt'),
    ('t-shirt', 't-shirt'),
    ('bag', 'bag'),
    ('glasses', 'glasses'),
    ('others', 'others'),
)


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to ='Product',blank = True)
    price = models.FloatField()
    category = models.CharField(max_length=255,choices = category)

    def __str__(self):
        return f"{self.name}"

class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()

    def __str__(self):
        return f'{self.product}  {self.quantity}'

class WishList(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'


