from django.test import TestCase

# Create your tests here.

from string import ascii_letters, digits, punctuation
from random import choices


def password(request):
    return ''.join(choices(list(ascii_letters), k=request))


print(password(12))
print(digits + 'qwerty')
print(punctuation)
print(type(ascii_letters))
