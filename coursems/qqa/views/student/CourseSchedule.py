from django.http import HttpResponse
from qqa.models import Course
from qqa.models import Student
from qqa.models import StudentCourse
from django.shortcuts import render, get_object_or_404

def index(request):
    # return HttpResponse("Nothing")
    # student_no = request.session['']  ## 由此获取学生id
    student_no = '123456' # test
    student = get_object_or_404(Student, pk=student_no)
    sc = StudentCourse.objects.filter(student=student)
        
    context = {
        'SC':sc
    }
    return render(request, 'student/CourseSchedule/index.html', context)    
