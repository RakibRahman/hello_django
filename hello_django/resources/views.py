from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Blog(req):
    return render(req,'hello.html')