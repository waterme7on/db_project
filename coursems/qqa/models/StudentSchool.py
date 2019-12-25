from django.db import models
from qqa.models.Student import Student
from qqa.models.School import School

class StudentSchool(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, unique=True)
    major = models.CharField(max_length = 15, verbose_name="专业")
    enrollmentDate = models.DateField(verbose_name="入学时间")

    
    def __str__(self):
        return str(self.student) + " is a student of " + str(self.school)
    
    class Meta:
        app_label = 'qqa'
        db_table = 'StudentSchool'