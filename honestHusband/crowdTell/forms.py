from django import forms
from django.forms import ModelForm, Form, FileField, CharField, Textarea

from .models import *


class PictureQuestionForm(Form):
    title = CharField()
    image = FileField()
    text = CharField(widget=Textarea)

    def __init__(self, *args, **kwargs):
        super(PictureQuestionForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'accept': 'image/*', 'capture': 'camera'})
        self.fields['image'].label = ''


class AnswerForm(ModelForm):
    vote = forms.TypedChoiceField(coerce=lambda x: bool(int(x)),
                   choices=((0, 'Your ass is fat :('), (1, 'Niiiiiiceee')),
                   widget=forms.RadioSelect
                )
    class Meta:
        model = Answer
        fields = ['vote', 'comment']