from django.db import models
from qqa.models import Student
from qqa.models import Courlas

class SelectRecord(models.Model):
    # 数据项定义
    student_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    student_grade = models.CharField(max_length=12)
    courlas_no = models.ForeignKey(Courlas, on_delete=models.CASCADE)
    submit_time = models.DateTimeField()
    phase = models.CharField(max_length=12)
    intention = models.IntegerField()

    # 功能
    def __str__(self): 
        return str(self.student_no) + " select " + str(self.courlas_no) + " at " + str(self.student_grade)

    # 元数据
    class Meta:
        app_label = 'qqa'
        db_table = 'SelectRecord'
        unique_together = ['student_no', 'courlas_no', 'student_grade']