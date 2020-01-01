from django.urls import path, include

from .views import *

urlpatterns = [
    path('student/',include([
        path('index', student.Index.index),
        path('courseSelect',student.CourseSelect.index, name='courseSelectIndex'),  # 选课主页面
        path('courseSchedule',student.CourseSchedule.index, name='courseSchedule'),
        path('courseTypeDetail/<str:course_type>', student.CourseSelect.type_detail, name='courseTypeDetail'),
        path('courseSelectSubmit', student.CourseSelect.select_course, name='courseSelection'),
        path('semesterSelect',student.CourseScoreRequest.index, name="semester"),
        path('score/<str:type>',student.CourseScoreRequest.score, name="score"),
        path('scoreSelect',student.CourseScoreRequest.scoreSelect, name="scoreSelect"),
        path('courseSearch/',student.CourseSearch.index, name="CourseSearch"),
        path('courseSearchResult',student.CourseSearch.get_search_result,name="get_result"),
    ])),
    path('teacher/',include([

    ])),
    path('admin/',include([
        path('courseChoose', admin.CourseChoose.index),
        path('courseDetail/<str:course_no>', admin.CourseChoose.courlasChoose, name='courseDetail'),
        path('courlasDetail/<str:courlas_no>', admin.CourseChoose.courlasDetail, name='courlasDetail'),
        path('courseModify/<str:course_no>', admin.CourseChoose.courseModify, name='courseModify'),
        path('courseModify/<str:course_no>/modify', admin.CourseChoose.courseModifying, name='courseModifying'),
        path('courseModify/<str:course_no>/result', admin.CourseChoose.courseModifyResult, name='courseModifyResult'),
        path('courseAdd',admin.CourseChoose.courseAdd, name='courseADD'),
        path('courseAddSubmit',admin.CourseChoose.courseAddSubmit,name="courseAddSubmit"),
        path('<str:course_no>/courlasAdd',admin.CourseChoose.courlas_add, name='courlasADD'),
        path('<str:course_no>/courseAddSubmit',admin.CourseChoose.courlasAddSubmit,name="courlasAddSubmit"),
        


    ])),
    path('index/',common.test.index), #未登录时共用的index
    path('test/',common.test.index), #测试模板的页面
    path('login/',common.UserManage.index), #登录页面
    path('logout/',common.UserManage.logout), #登出, 非页面

]
