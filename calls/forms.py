from django import forms
from . import models


class CreateCall(forms.ModelForm):
    class Meta:
        model = models.Call
        fields = ['page_count_b', 'page_count_c', 'error_code', 'action', 'external_number',
                  'date_start', 'date_finish', 'expenses', 'slug', 'thumb']


class CreateCustomer(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['name', 'address', 'post_code', 'note', 'slug']


class CreatePrinter(forms.ModelForm):
    class Meta:
        model = models.Printer
        fields = ['name', 'ser_num', 'slug']