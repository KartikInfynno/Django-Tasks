import email
from django.db import models
from Auths.models import My_User
from ckeditor.fields import RichTextField

class Blogger_Profile(models.Model):
    user = models.ForeignKey(My_User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_no = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to = 'Blogger_Profile')
    profession = models.CharField(max_length=255)
    github = models.URLField(max_length=255)
    twitter = models.URLField(max_length=255)
    instagram = models.URLField(max_length=255)
    facebook = models.URLField(max_length=255)

    def __str__(self):
        return self.name



class Blogs(models.Model):
    user = models.ForeignKey(My_User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Blogger_Profile, on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=255)
    pub_date = models.DateField(auto_now_add=True)
    b_image = models.ImageField(upload_to = 'Blogs')
    images = models.FileField(blank=True)
    descriptions = RichTextField(blank=True,null=True)
    is_approved = models.BooleanField(default=False)
    del_approve = models.BooleanField(default=False)
    count = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.user} : Blog {self.title}'


class PostImage(models.Model):
    post = models.ForeignKey(Blogs, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.title

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
