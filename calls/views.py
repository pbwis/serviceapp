from django.shortcuts import render
from .models import Call


def calls_list(request):
    calls = Call.objects.all()
    return render(request, 'calls/calls_list.html', {'calls': calls})


def call_detail(request, slug):
    call = Call.objects.get(slug=slug)
    return render(request, 'calls/call_detail.html', {'call': call})
