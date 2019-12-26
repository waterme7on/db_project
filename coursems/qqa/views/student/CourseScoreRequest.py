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
    
    #记录相应学期开的课程
    score_list = StudentCourse.objects.filter(semester = type)
    
    #计算平均成绩，可改为绩点。
    avg_score = 0
    credits = 0
    for s in score_list:
        avg_score = avg_score + s.score*s.course.course_score
        credits = credits + s.course.course_score
    avg_score = avg_score/credits

    context = { 
        "score_list":score_list,
        "avg_score":avg_score
    }
    return render(request,'student/CourseScoreRequest/score.html',context)

def scoreSelect(request):
    if(request.method == "POST" ):
        return HttpResponse("HELLO!")
    else:

        return("Nothing")
