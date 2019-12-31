from django.db import models
from qqa.models import Student
from qqa.models import Courlas

class StudentCourlas(models.Model):
    student_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    courlas_no = models.ForeignKey(Courlas, on_delete=models.CASCADE)
    # status = models.IntegerField()
    semester = models.CharField(max_length=10)
    # intention = models.IntegerField()

    def __str__(self):
        return str(self.student_no) + " select " + str(self.courlas_no)

    class Meta:
        app_label = 'qqa'
        db_table = 'StudentCourlas'
        unique_together = ['student_no', 'courlas_no', 'semester']