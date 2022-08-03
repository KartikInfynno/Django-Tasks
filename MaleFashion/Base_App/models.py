from django.db import models
from Auths.models import My_User
from My_Seller.models import Add_Product


class Cart(models.Model):
    user = models.ForeignKey(My_User,on_delete=models.CASCADE)
    product = models.ForeignKey(Add_Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()

    def __str__(self):
        return f'Cart {self.product} , {self.quantity}'

class WishList(models.Model):
    user = models.ForeignKey(My_User,on_delete=models.CASCADE)
    product = models.ForeignKey(Add_Product,on_delete=models.CASCADE)

    def __str__(self):
        return f'Wishlist {self.user} , {self.product}'


