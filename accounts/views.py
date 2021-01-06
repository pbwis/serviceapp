from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def signup_view(request):
    form = UserCreationForm(request.POST)
    return render(request, 'accounts/signup.html', {'form': form})
