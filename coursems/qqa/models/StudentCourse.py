from django.db import models
from qqa.models import Student
#from qqa.models import Teacher
from qqa.models import Course

<<<<<<< HEAD
class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    semester = models.CharField(max_length=15, verbose_name='学期')
    score = models.IntegerField(verbose_name='成绩', null=True, blank=True)
=======
class SC(models.Model):

    # 数据项的定义
    student_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_no = models.ForeignKey(Course, on_delete=models.CASCADE)
    #teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    semester_no = models.CharField(max_length=15, verbose_name='学期')
    score_no = models.IntegerField(verbose_name='成绩', null=True, blank=True)
>>>>>>> 95f83b6d22834e657b63230eaa83cae0412df421

    def __str__(self):
        return str(self.student_no)+"got "+str(self.score_no)+"in"+str(self.course_no)

    class Meta:
        app_label = 'qqa'
        db_table = 'StudentCourse'