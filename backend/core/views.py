from django.shortcuts import render
import string
from core.models import User
from django.utils.crypto import get_random_string

# Create your views here.

def create_user_random(cantidad):
    for x in range(cantidad):
        username = 'usuario_{}'.format(get_random_string(5, string.ascii_letters))
        email = '{}@miumg.com'.format(username)
        password = 'abc123/-'
        User.objects.create_user(
            username=username, email=email, password=password
            )
    return '{} Usuarios creados exitosamente..!'.format(cantidad)