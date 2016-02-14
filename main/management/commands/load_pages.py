from django.core.management.base import BaseCommand
from main.models import Page

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Load pages')
        Page.objects.all().delete()
        p = Page()
        p.text = 'test text'
        p.title = 'About me'
        p.alias = 'about-me'
        p.on_main = True
        p.save()

        p = Page()
        p.text = 'test text test text test text '
        p.title = 'Contact info'
        p.alias = 'contact'
        p.on_main = True
        p.save()

        p = Page()
        p.text = 'test text test text test text '
        p.title = 'Portfolio'
        p.alias = 'portfolio'
        p.on_main = True
        p.save()

        p = Page()
        p.text = 'Special offer Special offer Special offer Special offer'
        p.title = 'Special offer'
        p.alias = 'special'
        p.on_main = False
        p.save()