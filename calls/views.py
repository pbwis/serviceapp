from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Call
from django.contrib.auth.decorators import login_required
from .forms import CreateCall
from . import forms


def calls_list(request):
    calls = Call.objects.all()
    return render(request, 'calls/calls_list.html', {'calls': calls})


def call_detail(request, slug):
    call = Call.objects.get(slug=slug)
    return render(request, 'calls/call_detail.html', {'call': call})


@login_required(login_url='/accounts/login')
def call_create(request):
    if request.method == 'POST':
        form = forms.CreateCall(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('calls:call_detail')
    else:
        form = forms.CreateCall()
    return render(request, 'calls/call_create', {'form': form})
