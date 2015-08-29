from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.landing, name='landing'),
    url(r'^respondToQuestion/', views.respond_to_question, name='respond_to_question'),
]