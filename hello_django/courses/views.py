from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def course(req):
    coursesList =[
    {
        "course_id": 1,
        "course_name": "Introduction to Python",
        "instructor": "John Smith",
        "duration": 6,
        "image_url": "https://picsum.photos/200/300?random=2",
    },
    {
        "course_id": 2,
        "course_name": "Data Science Fundamentals",
        "instructor": "Jane Doe",
        "duration": 8,
        "image_url": "https://picsum.photos/200/300?random=12",
    },
    {
        "course_id": 3,
        "course_name": "Web Development with Django",
        "instructor": "Bob Johnson",
        "duration": 10,
        "image_url": "https://picsum.photos/200/300?random=20",
    },
    {
        "course_id": 4,
        "course_name": "Machine Learning Basics",
        "instructor": "Alice Williams",
        "duration": 7,
        "image_url": "https://picsum.photos/200/300?random=21",
    },
]
    return render(req,'home.html',context={'coursesList':coursesList})

def profile(req):
    print('req',req)
    return HttpResponse('welcome rakib')


def users(req):
    print('req',req)
    return HttpResponse('welcome users')

def categories(req):
    print('req',req)
    return HttpResponse('welcome categories')