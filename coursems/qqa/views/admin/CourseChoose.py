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
            course_list.append(course) #找到了所有这个学期，这个学校，所有本学院专业的course

    context={"course_list":course_list}
    


    return render(request, 'admin/CourseChoose/index.html', context)    


def courlasChoose(request, course_no):
    #找course-courlas表
    print(course_no)
    course = Course.objects.filter(course_no = course_no).first()
    course_name = course.course_name
    courlas_objs = Courlas.objects.filter(course_no = course_no)


    courlas_list = []
    for courlas in courlas_objs :
        text = courlas.time_location 
        courlas_no = courlas.courlas_no 
        courlas_list.append({"text":text, "course_no":courlas_objs} )
    
    context = {"courlas_list": courlas_list ,"course_no":course_no,"course_name":course_name}

    return render(request,"admin/CourseChoose/courlas_select.html",context)


def courlasDetail(request, courlas_no):
    return HttpResponse("hello")
    

def courseModify(request, course_no):
    #找course-courlas表
    print(course_no)

    course_obj = Course.objects.filter(course_no = course_no).first()
    print(course_no)
    
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




def courseAdd(request):


    return render(request,"admin/CourseChoose/course_add.html")


def courseAddSubmit(request):
    print( request.POST)
    course_name = request.POST["course_name"]
    course_credit = request.POST["course_credit"]
    class_no_str = request.POST["class_no"]
    is_partly_visible = request.POST["is_partly_visible"][0]

    class_no_list = class_no_str.split(",")
    for i in range(0, len(class_no_list) ):
        class_no = class_no_list[i].replace(" ","")
        class_no_list[i] = class_no

    print("********************",course_name,course_credit,class_no_list,is_partly_visible)


    #填写数据库需要的信息，将从数据库得到的信息进行处理
    #course_no  自动生成
    #course_name
    #credit 学分
    #syllabus #课程大纲的链接  #大纲让老师填写
    #is_partly_visible 
    # 如果是全校可看，那么就不填
    #如果是部分可看，那么要填授课对象，把元组插入到，partlyVisible中


    #得到表单输入以后，进行输入检查
    #course_name是否跟数据库里面的重名？ - 重名就弹出警告框
    #学分
    #syllabus可以用往年的大纲

    #partlyvisible
    #可以用往年的数据
    
    context = {
        "course_name":course_name,
        "course_credit":course_credit
    }

    return render(request,"admin/CourseChoose/course_add_submit.html",context)



def courlas_add(request,course_no):
    time_example = timezone.now()
    context={
        "course_no":course_no,
        "time_example":time_example
    }
    return render(request,"admin/CourseChoose/courlas_add.html",context)

def courlasAddSubmit(request,course_no):
    courlas_no = request.POST["courlas_no"]
    term = request.POST["term"]
    time_location = request.POST["time_loc"]
    course = Course.objects.filter(course_no=course_no).first()
    syllabus = course.syllabus
    course_name = course.course_name

    #----------要有一个处理输入的时间地点的功能--------

    #-----------------------------------------------
    courlas = Courlas(courlas_no = courlas_no, course_no = course, term = term, syllabus = syllabus, time_location = time_location)
    courlas.save()
    context={
        "term":term,
        "course_name":course_name,
        "courlas_no":courlas_no,
        "syllabus":syllabus,
        "time_location":time_location
    }
    # courlas_no = models.CharField(max_length=12, primary_key=True)  # 编号
    # course_no = models.ForeignKey(Course, on_delete=models.CASCADE)#由传入的参数直接得到
    # term = models.DateField(verbose_name="学期")
    # syllabus = models.CharField(max_length=15)  # 大纲（URL）#继承course的
    # time_location = models.CharField(max_length=120)
    '''
        time_location: {
        "num" : xx，
        "info": [  
            {"time":[ 0,  1 ]   ,  "location": "教一"  }  ,  {“time”：[ 15，16 ] ,   "location": "教三"   },   ]， 
        }  
    '''

    return render(request,"admin/CourseChoose/courlas_add_submit.html",context)