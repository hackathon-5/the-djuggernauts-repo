from django import forms
from django.forms import ModelForm, Form, FileField, CharField, Textarea

from .models import *


class PictureQuestionForm(ModelForm):
    class Meta:
        model = PictureQuestion
        fields = ['title', 'text', 'image']

    def __init__(self, *args, **kwargs):
        super(PictureQuestionForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'accept': 'image/*', 'capture': 'camera'})


class AnswerForm(ModelForm):
    vote = forms.BooleanField(required=False, initial=False)
    comment = forms.CharField(widget=forms.Textarea, label='')
    class Meta:
        model = Answer
        fields = ['vote', 'comment']
