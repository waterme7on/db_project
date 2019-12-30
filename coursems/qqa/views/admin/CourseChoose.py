from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.http import Http404
from django.urls import reverse



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
            program = Program.objects.filter(program_no = program_no).first()

            course = program.course_no#注意 这里的course_no并不是真正的course_no，而是一个course实体
            course_name = course.course_name
            course_list.append(course_name) #找到了所有这个学期，这个学校，所有本学院专业的course

    context={"course_list":course_list}
    


    return render(request, 'admin/CourseChoose/index.html', context)    


def courlasChoose(request, course_no):
    #找course-courlas表
    print(course_no)

    courlas_objs = Courlas.objects.filter(course_no = course_no)


    courlas_list = []
    for courlas in courlas_objs :
        text = courlas.time_location 
        courlas_no = courlas.courlas_no 
        courlas_list.append({"text":text, "course_no":courlas_objs} )
    
    context = {"courlas_list": courlas_list }

    return render(request,"admin/CourseChoose/courlas_select.html",context)
    

def courseModify(request, course_no):
    #找course-courlas表
    print(course_no)

    course_obj = Course.objects.filter(course_no = course_no)
    
    context = {"course_obj": course_obj }#直接传入要更改的course即可

    return render(request,"admin/CourseChoose/courseModify.html",context)


def courseModifying(request, course_no):
    course = get_object_or_404(Course, pk=course_no)

    modified_name = request.POST['course_name']
    modified_credits = request.POST['course_credits']
    modified_visible = request.POST['visible']
    course.course_name = modified_name
    course.credit = modified_credits
    course.is_partly_visible = modified_visible
    course.save()
        
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('courseModifyResult', args=(course_no,)))


def courseModifyResult(request, course_no):
    course_obj = Course.objects.filter(course_no = course_no)
    context = {"course_obj":course_obj}
    return render(request,"admin/CourseChoose/courseModifyResult.html",context)