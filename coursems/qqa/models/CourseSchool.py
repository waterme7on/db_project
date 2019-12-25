from django.db import models
from qqa.models.School import School
from qqa.models.Course import Course

class CourseSchool(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    major = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return str(self.school) + " has " + str(self.course)

    class Meta:
        app_label = 'qqa'
        db_table = 'CourseSchool'
        unique_together = ['school', 'course']