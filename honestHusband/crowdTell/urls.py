from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^photo/(?P<pk>\d+)/', PictureQuestionDetailView.as_view(), name="picture_detail"),
    url(r'^upload_picture/', PictureQuestionCreateView.as_view(), name="upload_picture"),
    url(r'^answer_question/(?P<question_id>\d+)/', AnswerCreateView.as_view(), name='answer_question'),
    url(r'^answer_random_question/', answer_random_question, name='answer_random_question'),
    url(r'^vote_result/(?P<question_id>\d+)/', submit_vote_result, name='submit_vote_result'),
    url(r'^person/(?P<pk>\d+)/', PersonDetailView.as_view(), name="person_detail"),
    url(r'person_bootstrapped/', bootstrapped_person_view, name="bootstrapped_person"),
    url(r'^create_person/', PersonCreateView.as_view(), name='create_person'),
    url(r'^search/', search, name='search'),
    url(r'^search_results/', search_results, name='search_results'),
    url(r'^add_friend', add_friend, name='add_friend'),
    url(r'^$', landing, name='landing'),
]