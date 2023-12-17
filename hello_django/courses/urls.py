from django.urls import path

from . import views


urlpatterns = [
    path('',views.course,name='home'),
    path('courses',views.top_courses,name='courses'),
]
