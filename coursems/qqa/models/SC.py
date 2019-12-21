from django.db import models
from .Student import Student
from .Teacher import Teacher
from .Course import Course
class SC(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    semester = models.CharField(max_length=15, verbose_name='学期')
    score = models.IntegerField(verbose_name='成绩', null=True, blank=True)

    def __str__(self):
        return self.semester

    class Meta:
        app_label = 'qqa'
        db_table = 'SC'