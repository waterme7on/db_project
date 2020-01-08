from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.http import Http404
from django.utils.timezone import now
from qqa.models import *

def index(request):
    course_types = MajorProgramCourse.COURSE_TYPE
    course_types = [c[1] for c in course_types]
    student_no = request.session['no']
    student = Student.objects.get(student_no = student_no)
    context = {
        'course_types': course_types,
        'name': student.student_name,
    }

    return render(request, 'student/CourseSelect/index.html', context)

def type_detail(request, course_type):
    # 首先得到学生所处学院的培养方案
    course_types = {c[1]:c[0] for c in MajorProgramCourse.COURSE_TYPE}
    course_type = course_types[course_type]
    # 根据课程类型，从学生所属学院的培养方案中筛选出培养方案的条目
    student_no = request.session['no']
    # student_no = '123456' # for testing
    student = Student.objects.get(student_no = student_no)
    # 找到学生所属班级和专业
    student_class = StudentClass.objects.get(student_no=student)
    major_no = Class.objects.get(pk=student_class.class_no).major_no
    # 从学生所属专业的培养方案中筛选出培养方案的条目
    program_set = MajorProgramCourse.objects.filter(course_type=course_type, major_no=major_no)
    # 根据培养方案条目中的课程找到教学班
    courlases = Courlas.objects.none()
    for tuple in program_set:
        tuple = tuple.course_no
        tmp_courlas_queryset = Courlas.objects.filter(course_no=tuple.course_no)
        courlases = courlases | tmp_courlas_queryset

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
        'name': student.student_name,
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
    selected_courlases = request.POST.getlist('courlas')   # django的Queryset利用这个获取列表
    select_intentions = request.POST.getlist('intention')
    # 首先在选课审核队列中加入表项
    # 紧接着由系统在后台进行选课处理

    # 以下为在数据库中添加元组
    student_no = request.session['no']
    # student_no = '123456' # for testing
    student = Student.objects.get(student_no = student_no)
    context['name'] = student.student_name
    term = str(timezone.now().year)
    if (int(timezone.now().month)) <= 8 :
        term += '春'
    else:
        term += '秋'
    phase = Phase.objects.filter(term=term)
    for p in phase:
        if p.beg_time <= now() and p.end_time >= now():
            phase = p 
            break
    for courlas_no in selected_courlases:
        # getlist 得到字符串数组
        # course_no = int(course_no)
        courlas = int(courlas_no.split(',')[1])
        courlas = Courlas.objects.get(courlas_no = courlas)
        intention = int(courlas_no.split(',')[0])
        intention = int(select_intentions[intention])
        try:
            # 判断是否有剩余名额
            left_num = courlas.max_select_num - courlas.selected_num
            assert(left_num > 0)
            sr = CurrentSelectRecord(student_no=student, courlas_no=courlas, intention=intention, submit_time=now(), phase=phase.phase, student_grade=student.grade)
            sr.save()
            courlas.selected_num += 1
            courlas.save()
            context['success'].append(courlas)
        except Exception as e:
            context['fail'].append(courlas)
            print('[Error:CourseSelect] ', e)
    return select_result(request, context)

def select_result(request, context):
    # print(context)
    return render(request, 'student/CourseSelect/select_result.html', context)

def course_history(request, course_no):
    course = Course.objects.get(course_no = course_no)
    courlases = Courlas.objects.filter(course_no=course)
    
    paginator = Paginator(courlases, 25)
    # print(paginator.num_pages)
    page = request.GET.get('page')
    student_no = request.session['no']
    student = Student.objects.get(student_no = student_no)
    try:
        courlases = paginator.page(page)
    except PageNotAnInteger:
        courlases = paginator.page(1)
    except EmptyPage:
        courlases = paginator.page(paginator.num_pages)
    context = {
        'courlases': courlases,
    }
    context['name'] = student.student_name
    return render(request, 'student/CourseSelect/history.html', context)    

    # return index(request)