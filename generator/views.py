import re
import math

from django.shortcuts import render
from .quantum_generator_emulator import QuantumGen

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    length = int(request.GET.get('length', 12))
    ascii_decimal_list = list(range(97, 123))

    if request.GET.get('uppercase'):
        ascii_decimal_list.extend(list(range(65, 91)))

    if request.GET.get('numbers'):
        ascii_decimal_list.extend(list(range(48, 57)))

    if request.GET.get('special'):
        ascii_decimal_list.extend(list(range(33, 48)))

    the_password = QuantumGen(length, ascii_decimal_list).generate_password()

    return render(request, 'generator/password.html', {'password': the_password})


def about(request):
    return render(request, 'generator/about.html')



