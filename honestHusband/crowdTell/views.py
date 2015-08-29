from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView, CreateView
from .models import *


class PictureCreateView(CreateView):
    model = Picture
    fields = ['image']
    template_name = 'crowdTell/picture_create_view.html'