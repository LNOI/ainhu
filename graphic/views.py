import imp
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from .models import Logs
from datetime import date, datetime
# Create your views here.

def home(request):
    return render(request,"base/index.html",{})

def lixi(request):
    if request.method=="GET":
        if not request.GET:
            print("Rong")
        else:
            if request.GET["phanthuong"]:
                now=datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                log=dt_string+"    "+request.GET["phanthuong"]
                logs={
                    'history':log
                }
                Logs.objects.create(**logs)

    return render(request,"base/lixi.html",{})
