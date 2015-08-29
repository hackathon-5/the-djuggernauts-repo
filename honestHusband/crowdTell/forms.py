from django import forms

from django.forms import ModelForm

from .models import *


class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(PictureForm, self).__init__(*args, **kwargs)
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