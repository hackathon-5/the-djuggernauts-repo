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
