from django.shortcuts import render,redirect
from django.http import HttpResponse

def Home(request):
    return render(request,'index.html')