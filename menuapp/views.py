from django.shortcuts import render
from . import models
from django.http import HttpResponse



def home(request):
    return render(request,'menuapp/home.html')
def indian(request):
    return render(request,'menuapp/indian.html')
def chinese(request):
    return render(request,'menuapp/chinese.html')
def vegindian(request):
    vegind=models.VegIndian()
    return render(request,'menuapp/vegindian.html',{'vegind':vegind})
