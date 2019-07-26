from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Photo

class Photos(ListView):
    model = Photo
    template_name = 'main.html'
    context_object_name ='photo_items'

class PhotoView(DetailView):
    model = Photo
    template_name = 'detail.html'
    
