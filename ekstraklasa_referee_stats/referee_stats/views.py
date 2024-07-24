from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Treść views.py")
