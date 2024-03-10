from django.http import HttpResponse
from django.shortcuts import render

def start(request):
    return render(request, "start.html", context={"text": "Аверьянов Максим Сергеевич РИ-220947"})

def poem(request):
    return render(request, "poem.html")



