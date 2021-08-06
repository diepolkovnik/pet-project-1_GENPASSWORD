from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):


    simbols = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        simbols.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        simbols.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        simbols.extend(list('0123456789'))

    length = int(request.GET.get('length', 14))

    thepass = ''

    for x in range(length):
        thepass += random.choice(simbols)

    

    return render(request, 'generator/password.html', {'pwd':thepass})
