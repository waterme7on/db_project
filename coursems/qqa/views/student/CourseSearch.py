from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from qqa.models import Course

from qqa.models import Teacher

from .forms import CourseSearchForm

def get_search_result(request):
    if(request.method == "POST" ):
        form = CourseSearchForm(request.POST)
        if form.is_valid() :
            course_no = form.cleaned_data["course_no"]
            course_name = form.cleaned_data["course_name"]
            teacher_no = form.cleaned_data["course_name"]
            teacher_name = form.cleaned_data["teacher_name"]
            course_semester = form.cleaned_data["course_semester"]
            course_school = form.cleaned_data["course_school"]

            #TODO 进行数据库的连接操作， 找出查询结果， 将结果返回给网页

            return HttpResponse("表单变量获取成功！")
        else: 
            
            return HttpResponse("表单变量获取失败！")


    return HttpResponse("HELLO!")

def index(request):
    #进入主页面，首先是搜索框阶段
    
    
    return render(request, 'student/CourseSearch/index.html',)
    

# def score(request, type):
#     # sem_types = {s[1]:s[0] for s in Course.SEMESTER_TYPE}
#     # sem_type = sem_types[type]
#     # print(sem_type)
#     #记录相应学期开的课程
#     score_list = StudentCourse.objects.filter(semester = type)
    
#     #存对应的学生-课程表里的记录
#     # score_list = []

#     # #做表连接查询
#     # for c in course_list:
#     #     sc_record = StudentCourse.objects.filter(course = c)
#     #     for sc in sc_record:
#     #         score_list.append(sc)

#     context = { 
#         "score_list":score_list
#     }
#     return render(request,'student/CourseScoreRequest/score.html',context)
