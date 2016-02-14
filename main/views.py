from django.shortcuts import render
from .models import Page, Gallery

# Create your views here.

def index(request):
    pages = Page.objects.filter(on_main=True)
    gallery = Gallery.objects.all()
    cntx = {'pages': pages, 'gallery': gallery}
    return render(request,'center.html', cntx)
