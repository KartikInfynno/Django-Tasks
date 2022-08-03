from django.db import models
from Auths.models import My_User

class Blogs(models.Model):
    user = models.ForeignKey(My_User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    pub_date = models.DateField(auto_now_add=True)
    b_image = models.ImageField(upload_to = 'Blogs')
    descriptions = models.TextField(max_length=255)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} : Blog {self.title}'



