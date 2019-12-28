from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.http import Http404



from qqa.models import Course
from qqa.models import Courlas
from qqa.models import Major
from qqa.models import MajorProgram
from qqa.models import Program
from qqa.models import School

def index(request):

    # 首先先获取教秘是什么学院的

    #先从school - major - program - course
    school_no = School.objects.filter(school_no = "1").first()
    semester = " "
    majors =  Major.objects.filter(school_no = school_no)
    course_list = []
    
    for major in majors :

        program_no_objs= MajorProgram.objects.filter(major_no = major.major_no)#还要加一个判断semester的条件 但是好像不能直接"and"
        for program_objs in program_no_objs :
            program_no = program_objs.program_no
            program = Program.objects.filter(program_no = program_no)
            course_no = program.course_no#注意 这里的course_no并不是真正的course_no，而是一个course实体
            course_list.append(course_no) #找到了所有这个学期，这个学校，所有本学院专业的course

    context={"course_list":course_list}
    




    return render(request, 'admin/CourseChoose/index.html', context)    
