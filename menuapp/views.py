from django.shortcuts import render, get_object_or_404
from . import models
from django.http import HttpResponse

def home(request):
    return render(request, 'menuapp/home.html')
def indian(request):
    return render(request, 'menuapp/indian.html')
def chinese(request):
    return render(request, 'menuapp/chinese.html')
def vegindian(request):
    vegiposts=models.VegIndian.objects.all()
    vegiargs={'vegiposts':vegiposts}
    return render(request,'menuapp/vegindian.html',vegiargs)
def nonvegindian(request):
    nonvegiposts=models.NonvegIndian.objects.all()
    nonvegiargs={'nonvegiposts':nonvegiposts}
    return render(request,'menuapp/nonvegindian.html',nonvegiargs)
def vegchinese(request):
    vegcposts=models.VegChinese.objects.all()
    vegcargs={'vegcposts':vegcposts}
    return render(request,'menuapp/vegchinese.html',vegcargs)
def nonvegchinese(request):
    nonvegcposts=models.NonvegChinese.objects.all()
    nonvegcargs={'nonvegcposts':nonvegcposts}
    return render(request,'menuapp/nonvegchinese.html',nonvegcargs)
