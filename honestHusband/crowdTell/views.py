from random import randrange
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import CreateView, DetailView
from registration.backends.simple.views import RegistrationView
from .forms import *
from .models import *


class PictureDetailView(DetailView):
    model = Picture
    context_object_name = 'picture'
    template_name = 'crowdTell/picture_detail_view.html'


class PictureCreateView(CreateView):
    form_class = PictureForm
    template_name = 'crowdTell/picture_create_view.html'

    def get_form(self, form_class=form_class):
        person = get_object_or_404(Person, user__id=self.request.user.id)
        form = super(PictureCreateView, self).get_form(form_class)
        form.instance.person = person
        form.label = ''
        return form


class PersonCreateView(CreateView):
    model = Person
    fields = ['first_name', 'last_name']
    template_name = 'crowdTell/generic_form.html'

    def get_form(self, form_class=None):
        form = super(PersonCreateView, self).get_form()
        form.instance.user = self.request.user
        return form

    def get_success_url(self):
        return reverse('crowdTell:upload_picture')


class AnswerCreateView(CreateView):
    model = Answer
    fields = ['vote', 'comment']

    def dispatch(self, request, *args, **kwargs):
        self.question = get_object_or_404(Question, pk=kwargs['question_id'])
        return super(AnswerCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super(AnswerCreateView, self).get_context_data(**kwargs)
        context_data['question'] = self.question
        return context_data

    def get_form(self, form_class=None):
        form = super(AnswerCreateView, self).get_form()
        form.instance.person = get_object_or_404(Person, user__id=self.request.user.id)
        form.instance.question = self.question



def landing(request):
    return render(request, 'crowdTell/landing.html', {})


def submit_vote_result(request):
    vote_result = request.POST['vote_result']
    return render(request, 'crowdTell/submit_vote_view.html', {'vote_result': vote_result})


class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return reverse('crowdTell:create_person',)
    
    
def find_friends(request):
    return render(request, 'crowdTell/find_friends_view.html', {})


def search_for_friends(request):
    friend_username = request.POST['username']
    friend_result = Person.objects.get(user__username=friend_username)
    return render(request, 'crowdTell/search_for_friends_view.html', {'friend_username': friend_result})

def answer_random_question(request):
    number_of_questions = Question.objects.all().count()
    question_id = randrange(1, number_of_questions + 1)
    return HttpResponseRedirect(reverse('crowdTell:answer_question', args=(question_id,)))