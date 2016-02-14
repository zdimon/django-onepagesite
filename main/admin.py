from django.contrib import admin
from image_cropping import ImageCroppingMixin

# Register your models here.
from .models import Page, Gallery

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','text', 'alias')
   
admin.site.register(Page, PageAdmin)


class GalleryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('get_thumbnail','image')
   
admin.site.register(Gallery, GalleryAdmin)

