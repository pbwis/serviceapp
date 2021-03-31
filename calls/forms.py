from django import forms
from . import models


class CreateCall(forms.ModelForm):
    class Meta:
        model = models.Call
        fields = ['page_count_b', 'page_count_c',
                  'error_code', 'action', 'external_number', 'date_start', 'date_estimate', 'date_finish', 'expenses', 'slug', 'thumb']


class EditCall(forms.ModelForm):
    class Meta:
        model = models.Call
        fields = ['page_count_b', 'page_count_c',
                  'error_code', 'action', 'external_number', 'date_start', 'date_estimate', 'date_finish',  'expenses', 'thumb']


class DeleteCall(forms.ModelForm):
    class Meta:
        model = models.Call
        fields = []


class CreateCustomer(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['name', 'address', 'post_code', 'note', 'slug']


class CreatePrinter(forms.ModelForm):
    class Meta:
        model = models.Printer
        fields = ['name', 'ser_num', 'slug']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.TypeOfDevice
        exclude = ['']


class EstTimeForm(forms.ModelForm):
    class Meta:
        model = models.TypeOfEstTime
        exclude = ['']