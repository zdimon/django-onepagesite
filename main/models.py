from django.db import models
from image_cropping.fields import ImageRatioField, ImageCropField
from easy_thumbnails.files import get_thumbnailer
from django.utils.safestring import mark_safe
# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    alias = models.CharField(max_length=50, blank=True, null=True)
    text = models.TextField()
    on_main = models.BooleanField(default=False)


class Gallery(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    image = ImageCropField(upload_to='gallery')
    cropping = ImageRatioField('image', '100x100')

    @property
    def get_thumbnail(self):
        url = get_thumbnailer(self.image).get_thumbnail({
            'size': (100, 100),
            'box': self.cropping,
            'crop': 'smart',            
        }).url
        return mark_safe('<img src="%s" />' % url)
