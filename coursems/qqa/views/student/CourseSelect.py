from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from qqa.models import Course
from qqa.models import Student
from qqa.models import StudentCourse
from django.utils import timezone

def index(request):
    course_types = Course.COURSE_TYPE
    course_types = [c[1] for c in course_types]
    context = {
        'course_types': course_types,
    }
    return render(request, 'student/CourseSelect/index.html', context)

def type_detail(request, course_type):
    course_types = {c[1]:c[0] for c in Course.COURSE_TYPE}
    course_type = course_types[course_type]
    courses = Course.objects.filter(course_type=course_type)
    context = {
        'courses': courses,
    }
    return render(request, 'student/CourseSelect/type_detail.html', context)    

def select_course(request):
    context = {
        'success':[],
        'fail':[]
    }
    if request.method == 'POST':
        print(request.POST) # <QueryDict: {'csrfmiddlewaretoken': ['fsSPEwr8oi01TtjHBItUECNbRw9V5oL58JVrPb4avFBzU6kLELGcJZOGVbTf9OV7'], 'course': ['3']}>
        selected_courses = request.POST.getlist('course')   # django的Queryset利用这个获取列表
        # 首先在选课审核队列中加入表项
        # 紧接着由系统在后台进行选课处理

        # 以下为在数据库中添加元组
        # student_no = request.session['student_no']
        student_no = '123456' # for testing
        student = Student.objects.get(student_no = student_no)

        semester = str(timezone.now().year)+"/"+str(timezone.now().month)
        
        for course_no in selected_courses:
            # getlist 得到字符串数组
            # course_no = int(course_no)
            course = Course.objects.get(course_no = course_no)
            try:
                StudentCourse.add_tuple(student=student, course=course, semester=semester)
                context['success'].append(course)
            except:
                context['fail'].append(course)
            # sc = StudentCourse(student_no = student_no, course_no = course)
            # sc.save()

        return select_result(request, context)

def select_result(request, context):
    print(context)
    return render(request, 'student/CourseSelect/select_result.html', context)