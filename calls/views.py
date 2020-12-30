from django.shortcuts import render


def calls_list(request):
    return render(request, 'calls/calls_list.html')