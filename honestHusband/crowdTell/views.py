from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import CreateView, DetailView
from .models import *


class PictureDetailView(DetailView):
    model = Picture
    context_object_name = 'picture'
    template_name = 'crowdTell/picture_detail_view.html'


class PictureCreateView(CreateView):
    model = Picture
    fields = ['image']
    template_name = 'crowdTell/picture_create_view.html'

    def get_form(self, form_class=None):
        person = get_object_or_404(Person, user__id=self.request.user.id)
        form = super(PictureCreateView, self).get_form()
        form.instance.person = person
        return form


def respond_to_question(request):
    try:
        question_id = request.GET['question_id']
        random_question = Question.objects.get(pk=question_id)
    except:
        random_question = Question.objects.order_by('?').first()

    return render(request, 'crowdTell/picture_vote_view.html', {'question': random_question})


def landing(request):
    return render(request, 'crowdTell/landing.html', {})


def submit_vote_result(request):
    vote_result = request.POST['vote_result']
    return render(request, 'crowdTell/submit_vote_view.html', {'vote_result': vote_result})