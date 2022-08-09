from django.contrib import admin
from .models import Blogs,Comments,Fav_Blogs,IP_Model
# Register your models here.


admin.site.register(Blogs)
admin.site.register(Comments)
admin.site.register(Fav_Blogs)
admin.site.register(IP_Model)
