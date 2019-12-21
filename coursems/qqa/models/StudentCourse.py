from django.db import models
from .Student import Student
from .Teacher import Teacher
from .Course import Course

class SC(models.Model):

    # 数据项的定义
    student_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_no = models.ForeignKey(Course, on_delete=models.CASCADE)
    #teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    semester_no = models.CharField(max_length=15, verbose_name='学期')
    score_no = models.IntegerField(verbose_name='成绩', null=True, blank=True)

    def __str__(self):
        return self.semester_no

    class Meta:
        app_label = 'qqa'
        db_table = 'SC'