# from Course import Course
# from Teacher import Teacher
from django.db import models
from qqa.models import Course 
from qqa.models import Teacher

class TC(models.Model):
    #课程-教师表 
    course_no = models.ForeignKey(Course, on_delete = models.CASCADE)
    teacher_no = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    def __str__(self):
        return str(self.course_no)+"is taught by "+str(self.teacher_no)
    
    class Meta:
        app_label = 'qqa'
        db_table = "TC"


        