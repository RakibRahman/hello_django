from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def course(req):
    print('req',req)
    return HttpResponse('welcome to Django')

def profile(req):
    print('req',req)
    return HttpResponse('welcome rakib')