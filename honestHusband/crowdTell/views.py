from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from .models import *


class PictureCreateView(CreateView):
    model = Picture
    fields = ['image']
    template_name = 'crowdTell/picture_create_view.html'


def respond_to_question(request):
    random_question = Question.objects.order_by('?').first()
    return render(request, 'crowdTell/picture_vote_view.html', {'question': random_question})

def landing(request):
    return render(request, 'crowdTell/landing.html', {})