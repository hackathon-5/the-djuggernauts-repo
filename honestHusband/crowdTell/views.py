from random import randrange

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


# Create your views here.
from django.views.generic import CreateView, DetailView
from registration.backends.simple.views import RegistrationView
from .forms import *
from .models import *


class PictureQuestionDetailView(DetailView):
    model = PictureQuestion
    context_object_name = 'picture'
    template_name = 'crowdTell/picture_detail_view.html'


class PictureQuestionCreateView(CreateView):
    form_class = PictureQuestionForm
    template_name = 'crowdTell/picture_create_view.html'

    def get_form(self, form_class=form_class):
        form = super(PictureQuestionCreateView, self).get_form(form_class)
        form.instance.person = get_object_or_404(Person, user__id=self.request.user.id)
        return form


class PersonDetailView(DetailView):
    model = Person
    context_object_name = 'person'
    template_name = 'crowdTell/person_detail_view.html'


def bootstrapped_person_view(request):
    person = get_object_or_404(Person, user__id=request.user.id)
    return HttpResponseRedirect(reverse('crowdTell:person_detail', args=(person.id,)))

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
    form_class = AnswerForm
    template_name = 'crowdTell/answer_create_view.html'

    def dispatch(self, request, *args, **kwargs):
        self.picture_question = get_object_or_404(PictureQuestion, pk=kwargs['question_id'])
        return super(AnswerCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super(AnswerCreateView, self).get_context_data(**kwargs)
        context_data['picture_question'] = self.picture_question
        return context_data

    def get_form(self, form_class=None):
        form = super(AnswerCreateView, self).get_form()
        form.instance.person = get_object_or_404(Person, user__id=self.request.user.id)
        form.instance.question = self.picture_question
        return form


def landing(request):
    return render(request, 'crowdTell/landing.html', {})


def submit_vote_result(request, *args, **kwargs):
    picture_question = get_object_or_404(PictureQuestion, pk=kwargs['question_id'])
    return render(request, 'crowdTell/submit_vote_view.html', {'picture_question': picture_question})


class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return reverse('crowdTell:create_person',)


def answer_random_question(request):
    number_of_questions = PictureQuestion.objects.all().count()
    question_id = randrange(1, number_of_questions + 1)
    return HttpResponseRedirect(reverse('crowdTell:answer_question', args=(question_id,)))
