# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def holla(request):
    return HttpResponse('<h1>Bem vindo a minha AGENDA.</h1>')