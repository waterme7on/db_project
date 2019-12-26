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
            context = {
                "courses" : [{"course_no":"1", "course_name":"数学分析","teacher_name":"孟岩","course_semester":"2019年夏季","course_credit":"4","student_number":"40"},{"course_no":"2", "course_name":"实变函数","teacher_name":"孟岩","course_semester":"2019年夏季","course_credit":"4","student_number":"40"}]
            }

            return render(request,"student/CourseSearch/search_result.html",context)
        else: 
            
            return HttpResponse("表单变量获取失败！")


    return HttpResponse("HELLO!")

def index(request):
    #进入主页面，首先是搜索框阶段
    
    
    return render(request, 'student/CourseSearch/index.html',)
    