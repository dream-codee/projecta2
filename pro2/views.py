from django.http import HttpResponse
from django.shortcuts import render



def demo2(request):
    return render(request, "demo1.html")