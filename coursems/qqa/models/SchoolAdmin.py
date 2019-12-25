from django.db import models
from qqa.models.School import School
from qqa.models.Teacher import Teacher

class SchoolAdmin(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, unique=True)
    admin = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.school) + "'s admin is " + str(self.admin)

    class Meta:
        app_label = 'qqa'
        db_table = 'SchoolAdmin'
        