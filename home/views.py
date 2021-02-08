from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def home(request):
    home =models.Last_Projects.objects.all()

    return render(request , 'home/home.html' , {'object' : home})
