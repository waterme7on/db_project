from django.db import models
from qqa.models import Major
from qqa.models import Class

class ClassMajor(models.Model):
    class_no = models.ForeignKey(Class, on_delete=models.CASCADE)
    major_no = models.ForeignKey(Major, on_delete=models.CASCADE) 

    def __str__(self):
        return str(self.class_no) + " in " + str(self.major_no)

    class Meta:
        app_label = 'qqa'
        db_table = 'ClassMajor'
        unique_together = ['class_no', 'major_no']