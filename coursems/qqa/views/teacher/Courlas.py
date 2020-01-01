from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from qqa.models import Teacher
from qqa.models import TeacherCourlas
from qqa.models import StudentCourlas
from qqa.models import Course
from qqa.models import Courlas

def index(request):
    # 教师查看每学期有哪些课
    if request.session:
        tno = request.session["no"]
        tcourlas = TeacherCourlas.objects.filter(teacher_no=tno)
        courlases_list = [] # 存字典 [ {"courlas_no": "" , "courlas_name" : "" , "term": ""}]
        if tcourlas.exists():
            for tc in tcourlas:
                courlas_dict = {}
                courlas_dict["courlas_no"] = tc.courlas_no
                courlas = Courlas.objects.get(courlas_no=tc.courlas_no)
                courlas_dict["term"] = courlas.term
                course = Course.objects.get(courlas_no=courlas.course_no)
                courlas_dict["courlas_name"] = course.course_name
                courlases_list.append(courlas_dict)
            return render(request,"teacher/courlas_index.html",{"courlases": courlases_list})       
    
    return render(request,"teacher/courlas_index.html",{})
    pass

def detail(request, courlas_no):
    pass