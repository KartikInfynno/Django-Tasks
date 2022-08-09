import email
from django.db import models
from Auths.models import My_User
from ckeditor.fields import RichTextField

class Blogs(models.Model):
    user = models.ForeignKey(My_User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    pub_date = models.DateField(auto_now_add=True)
    b_image = models.ImageField(upload_to = 'Blogs')
    descriptions = RichTextField(blank=True,null=True)
    is_approved = models.BooleanField(default=False)
    del_approve = models.BooleanField(default=False)
    count = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.user} : Blog {self.title}'

class Fav_Blogs(models.Model):
    user = models.ForeignKey(My_User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} : Fav {self.blog}'

class Comments(models.Model):
    user = models.ForeignKey(My_User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comment = models.TextField(max_length=255)
    post_date = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'User : {self.user} : Comments {self.comment} Status: {self.is_approved}'

class IP_Model(models.Model):
    ip = models.CharField(max_length=40)
    user = models.ForeignKey(My_User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ip} {self.user} {self.blog}'
