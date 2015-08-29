from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^photo/(?P<pk>\d+)/', PictureDetailView.as_view(), name="picture_detail"),
    url(r'^upload_picture/', PictureCreateView.as_view(), name="upload_picture"),
    url(r'^answer_question/(?P<question_id>\d+)/', AnswerCreateView.as_view(), name='answer_question'),
    url(r'^answer_random_question', answer_random_question, name='answer_random_question'),
    url(r'^vote_result/', submit_vote_result, name='submit_vote_result'),
    url(r'^create_person/', PersonCreateView.as_view(), name='create_person'),
    url(r'^find_friends', find_friends, name='find_friends'),
    url(r'^search_for_friends', search_for_friends, name='search_for_friends'),
    url(r'^$', landing, name='landing'),
]