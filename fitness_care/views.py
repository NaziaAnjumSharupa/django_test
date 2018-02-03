from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    text = "Fitness care gym"
    return HttpResponse(text)