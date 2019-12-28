from django.db import models
from qqa.models import Courlas
from qqa.models import Class

class PartlyVisible(models.Model):
    courlas_no = models.ForeignKey(Courlas, on_delete=models.CASCADE)  # 一个班内多个学生，故用一对多
    class_no = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.courlas_no) + " - " + str(self.class_no)

    class Meta:
        app_label = 'qqa'
        db_table = 'PartlyVisible'
        unique_together = ['courlas_no', 'class_no']