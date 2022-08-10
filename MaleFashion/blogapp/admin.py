from django.contrib import admin
from .models import Blogger_Profile, Blogs,Comments,Fav_Blogs,IP_Model,PostImage
# Register your models here.


admin.site.register(Blogs)
admin.site.register(Comments)
admin.site.register(Fav_Blogs)
admin.site.register(IP_Model)
admin.site.register(Blogger_Profile)


class PostImageAdmin(admin.StackedInline):
    model = PostImage


class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Blogs

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

