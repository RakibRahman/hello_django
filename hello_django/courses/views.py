from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def course(req):
    print('req',req)
    return render(req,'home.html')

def profile(req):
    print('req',req)
    return HttpResponse('welcome rakib')


def users(req):
    print('req',req)
    return HttpResponse('welcome users')

def categories(req):
    print('req',req)
    return HttpResponse('welcome categories')