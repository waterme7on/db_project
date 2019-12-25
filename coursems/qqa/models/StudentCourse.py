from django.db import models
from qqa.models.Student import Student
from qqa.models.Teacher import Teacher
from qqa.models.Course import Course

class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    semester = models.CharField(max_length=15, verbose_name='学期')
    score = models.IntegerField(verbose_name='成绩', null=True, blank=True)

    def __str__(self):
        return str(self.student) + " selected " + str(self.course)

    def add_tuple(student_no, course_no):
        student = Student.objects.get(student_no = student_no)
        course = Course.objects.get(course_no = course_no)
        sc = StudentCourse(student = student, course = course)
        sc.save()


    class Meta:
        app_label = 'qqa'
        db_table = 'StudentCourse'