# from Course import Course
# from Teacher import Teacher
from django.db import models
from qqa.models import Course 
from qqa.models import Teacher

class TeacherCourse(models.Model):
    #课程-教师表 
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    semester = models.CharField(max_length=15, verbose_name='学期', blank=True)

    def __str__(self):
        return str(self.course_no)+"is taught by "+str(self.teacher_no)
    
    class Meta:
        app_label = 'qqa'
        db_table = "TeacherCourse"
        unique_together = ['teacher', 'course', 'semester']


        