from django.shortcuts import render
from django.http import HttpResponse

from string import ascii_letters, ascii_lowercase, digits, punctuation
from random import choices

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    length = int(request.GET.get('length', 12))
    chars = ascii_lowercase

    if request.GET.get('uppercase'):
        chars = ascii_letters

    if request.GET.get('numbers'):
        chars += digits

    if request.GET.get('special'):
        chars += punctuation

    the_password = ''.join(choices(list(chars), k=length))

    return render(request, 'generator/password.html', {'password': the_password})


def about(request):
    return render(request, 'generator/about.html')
