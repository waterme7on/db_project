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
        path('scoreSelect',student.CourseScoreRequest.scoreSelect, name="scoreSelect"),
        path('courseSearch/',student.CourseSearch.index, name="CourseSearch"),
        path('courseSearch/courseSearchResult',student.CourseSearch.get_search_result,name="get_result"),
    ])),
    path('teacher/',include([

    ])),
    path('admin/',include([

    ])),
    path('index/',common.test.index), #未登录时共用的index
    path('test/',common.test.index), #测试模板的页面
    path('login/',common.UserManage.index), #登录页面
    path('logout/',common.UserManage.logout), #登出, 非页面

]
