from django import forms
from .models import FileModel, ProfileTask

from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()


class MyForm(forms.ModelForm):
    my_field = forms.BooleanField(label='принято')

    class Meta:
        model = ProfileTask
        fields = ['my_field']
