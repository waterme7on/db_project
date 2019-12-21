from django.http import HttpResponse
from django.template import loader

from qqa.models import Course

def index(request):
    template = loader.get_template('SelectCourse/index.html')
    course_types = Course.COURSE_TYPE
    course_types = [c[1] for c in course_types]
    context = {
        'course_types': course_types,
    }
    return HttpResponse(template.render(context, request))

def type_detail(request, course_type):
    template = loader.get_template('SelectCourse/type_detail.html')
    course_types = {c[1]:c[0] for c in Course.COURSE_TYPE}
    course_type = course_types[course_type]
    courses = Course.objects.filter(course_type=course_type)
    context = {
        'courses': courses,
    }
    return HttpResponse(template.render(context, request))
    
