from django.db import models
from qqa.models import Teacher
from qqa.models import Courlas

class TeacherCourlas(models.Model):
    teacher_no = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    courlas_no = models.ManyToManyField(Courlas)

    def __str__(self):
        return str(self.teacher_no) + " teach " + str(self.courlas_no)

    class Meta:
        app_label = 'qqa'
        db_table = 'TeacherCourlas'
        # unique_together = ['student_no', 'courlas_no', 'semester']