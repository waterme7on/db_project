from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.http import Http404

from qqa.models import Course
from qqa.models import Courlas
from qqa.models import Student
from qqa.models import StudentCourlas
from qqa.models import Program

def index(request):
    course_types = Program.COURSE_TYPE
    course_types = [c[1] for c in course_types]
    context = {
        'course_types': course_types,
    }
    # print(request.session['no'])
    # print(request.session['character'])
    return render(request, 'student/CourseSelect/index.html', context)

def type_detail(request, course_type):
<<<<<<< HEAD
    # 首先得到学生所处学院的培养方案
=======
>>>>>>> ba5ac8f00c2cd2036a4909d2e6f64d12eaac7514
    course_types = {c[1]:c[0] for c in Program.COURSE_TYPE}
    course_type = course_types[course_type]
    # 根据课程类型，从学生所属学院的培养方案中筛选出培养方案的条目
    program_set = Program.objects.filter(course_type=course_type)
    courses = Program.objects.filter(course_type=course_type)
    # 根据培养方案条目中的课程找到教学班
    # courlases = []
    courlases = Courlas.objects.none()
    for tuple in program_set:
        tuple = tuple.course_no
        # print(tuple.course_no)
        tmp_courlas_queryset = Courlas.objects.filter(course_no=tuple.course_no)
        # courlases.append(tmp_courlas_queryset)
        courlases = courlases | tmp_courlas_queryset
    print(courlases)

    
    paginator = Paginator(courlases, 25)
    # print(paginator.num_pages)
    page = request.GET.get('page')
    try:
        courlases = paginator.page(page)
    except PageNotAnInteger:
        courlases = paginator.page(1)
    except EmptyPage:
        courlases = paginator.page(paginator.num_pages)
    context = {
        'courlases': courlases,
    }
    return render(request, 'student/CourseSelect/type_detail.html', context)    

def select_course(request):
    context = {
        'success':[],
        'fail':[],
        'prev': request.META.get('HTTP_REFERER')
    }
    # print(request.META.get('HTTP_REFERER'))
    if request.method != 'POST':
        Http404('Expect POST Method')

    # print(request.POST) # <QueryDict: {'csrfmiddlewaretoken': ['fsSPEwr8oi01TtjHBItUECNbRw9V5oL58JVrPb4avFBzU6kLELGcJZOGVbTf9OV7'], 'course': ['3']}>
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
    # print(context)
    return render(request, 'student/CourseSelect/select_result.html', context)