from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    return render(request,"base/index.html",{})

def lixi(request):
    return render(request,"base/lixi.html",{})
