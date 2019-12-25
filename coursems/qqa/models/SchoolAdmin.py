from django.db import models
from qqa.models.School import School
from qqa.models.Teacher import Teacher

class SchoolAdmin(models.Model):
    admin_no = models.CharField(max_length=12, primary_key=True, unique=True)
    admin_name =  models.CharField(max_length=20)
    password = models.CharField(max_length=100, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return str(self.school) + "'s admin is " + str(self.admin)

    class Meta:
        app_label = 'qqa'
        db_table = 'SchoolAdmin'
        