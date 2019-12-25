from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from qqa.models import Course
from qqa.models import StudentCourse

def index(request):
    
    semesters=[]
    semesters_tmp=[]
    records = StudentCourse.objects.all()
    for re in records:   
        semester = re.semester
        semesters_tmp.append(semester)
    s_tmp=set(semesters_tmp)
    semesters=list(s_tmp)
    
    
    context = {
        'semesters':semesters
    }
    
    #print(semesters)
    return render(request, 'student/CourseScoreRequest/index.html',context )
    

def score(request, type):
    # sem_types = {s[1]:s[0] for s in Course.SEMESTER_TYPE}
    # sem_type = sem_types[type]
    # print(sem_type)
    #记录相应学期开的课程
    score_list = StudentCourse.objects.filter(semester = type)
    
    #存对应的学生-课程表里的记录
    # score_list = []

    # #做表连接查询
    # for c in course_list:
    #     sc_record = StudentCourse.objects.filter(course = c)
    #     for sc in sc_record:
    #         score_list.append(sc)

    context = { 
        "score_list":score_list
    }
    return render(request,'student/CourseScoreRequest/score.html',context)
