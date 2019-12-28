from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from qqa.models import Course
from qqa.models import StudentCourlas

def index(request):
    
    semesters=[]
    semesters_tmp=[]
    records = StudentCourlas.objects.all()
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
    
    #student=.....记录登陆的学生

    #记录相应学期开的课程，应该还要有一个条件就是 student.student_no = record.student.student_no
    score_list = StudentCourse.objects.filter(semester = type)

    
    
    #计算平均成绩，可改为绩点。
    avg_score = 0
    credits = 0
    ZYBX_credits=0
    ZYXX_credits=0
    for s in score_list:
        avg_score = avg_score + s.score*s.course.course_score
        credits = credits + s.course.course_score
        if s.course.course_type == 'ZYBX':#后面应该再加上一个判断条件就是这个专业必修课的专业是该学生的专业
            ZYBX_credits = ZYBX_credits + s.course.course_score
        else:
            ZYXX_credits = ZYXX_credits + s.course.course_score
    avg_score = avg_score/credits

    context = { 
        "score_list":score_list,
        "avg_score":avg_score,
        "ZYBX_credits":ZYBX_credits,
        "ZYXX_credits":ZYXX_credits,
        "credits":credits
    }
    return render(request,'student/CourseScoreRequest/score.html',context)

def scoreSelect(request):
    if(request.method == "POST" ):
        return HttpResponse("HELLO!")
    else:

        return("Nothing")
