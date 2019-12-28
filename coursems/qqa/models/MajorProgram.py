from django.db import models
from qqa.models import Major
from qqa.models import Program

class MajorProgram(models.Model):
    major_no = models.ForeignKey(Major, on_delete=models.CASCADE) 
    program_no = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.major_no) + " - " + str(self.program_no)

    class Meta:
        app_label = 'qqa'
        db_table = 'MajorProgram'
        unique_together = ['major_no', 'program_no']