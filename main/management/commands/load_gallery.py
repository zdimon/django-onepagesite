from django.core.management.base import BaseCommand
from main.models import Gallery
from prj.settings import BASE_DIR
from django.core.files import File


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Load gallery')
        Gallery.objects.all().delete()
        for cnt in range(1,4):
            path = BASE_DIR+'/test_gallery/%s.jpg' % cnt
            print(path)
            with open(path, 'rb') as image:
                p = Gallery()
                p.title = 'image %s' % cnt
                p.image.save('%s.jpeg' % cnt, File(image), save=True)
                p.save()
            
