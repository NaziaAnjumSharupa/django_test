from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # text = "Fitness care gym"
    # return HttpResponse(text)
    context_dict = {}
    context_dict["name"] = "sharupa"
    return render(request,"fitness_care/index.html",context = context_dict)


def test(request):
     return render(request,"fitness_care/test.html")

def pic(request):
    return render(request,"fitness_care/pic.css")