from django.shortcuts import render
from .models import Call


def calls_list(request):
    calls = Call.objects.all()
    return render(request, 'calls/calls_list.html', {'calls': calls})