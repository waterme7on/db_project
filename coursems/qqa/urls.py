from django.urls import path

from .views import *

urlpatterns = [
    path('', CommonView.index, name='index'),
    path('SelectCourse/', SelectCourse.index, name='SelectCourseIndex'),
]
