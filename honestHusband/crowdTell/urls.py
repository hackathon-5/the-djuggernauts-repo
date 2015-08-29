from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^photo/(?P<pk>\d+)/', PictureDetailView.as_view(), name="picture_detail"),
    url(r'^upload_picture/', PictureCreateView.as_view(), name="upload_picture"),
    url(r'^respond_to_question/', views.respond_to_question, name='respond_to_question'),
    url(r'^vote_result/', views.submit_vote_result, name='submit_vote_result'),
    url(r'', landing, name='landing'),
]