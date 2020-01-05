from django.db import models
from qqa.models import Student
from qqa.models import Class

class StudentClass(models.Model):
    student_no = models.ForeignKey(Student, on_delete=models.CASCADE)  # 一个班内多个学生，故用一对多
    class_no = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student_no) + " in " + str(self.class_no)

    class Meta:
        app_label = 'qqa'
        db_table = 'StudentClass'
        unique_together = ['student_no', 'class_no']