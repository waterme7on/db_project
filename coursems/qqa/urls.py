from django.urls import path, include

from .views import *

urlpatterns = [
    path('student/',include([
        path('index',student.Index.index),
        path('courseSelect',student.CourseSelect.index),
        path('courseSchedule',student.CourseSelect.index),
        path('courseTypeDetail/<str:course_type>', student.CourseSelect.type_detail, name='courseTypeDetail'),
        path('courseSelectSubmit', student.CourseSelect.select_course, name='courseSelection'),
        path('semesterSelect',student.CourseScoreRequest.index, name="semester"),
        path('score/<str:type>',student.CourseScoreRequest.score, name="score"),
        path('courseSearch/',student.CourseSearch.index, name="CourseSearch"),
        path('courseSearchResult',student.CourseSearch.get_search_result,name="get_result"),
    ])),
    path('teacher/',include([

    ])),
    path('admin/',include([

    ])),
    path('test/',common.test.index),
]
