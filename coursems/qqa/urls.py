from django.urls import path, include

from .views import *

urlpatterns = [
    path('student/',include([
        path('index',student.Index.index),
        path('courseSelect',student.CourseSelect.index),
        path('courseSchedule',student.CourseSelect.index),
    ])),
    path('teacher/',include([

    ])),
    path('admin/',include([

    ])),
]
