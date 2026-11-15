from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Recipe App!")


def contato(request):
    return HttpResponse("Página de contato")


def sobre(request):
    return HttpResponse("Página sobre nós.")