from django import forms
from . import models


class CreateCall(forms.ModelForm):
    class Meta:
        model = models.Call
        fields = ['printer', 'page_count_b', 'page_count_c', 'action', 'slug', 'thumb']
