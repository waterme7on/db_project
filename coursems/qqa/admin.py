from django.contrib import admin
from .models.Course import Course
from .models.Student import Student
from .models.Teacher import Teacher
from .models.School import School
from .models.TeacherCourse import TeacherCourse
from .models.StudentCourse import StudentCourse
from .models.CourseSchool import CourseSchool
from .models.SchoolAdmin import SchoolAdmin
from .models.StudentSchool import StudentSchool


# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(School)
admin.site.register(TeacherCourse)
admin.site.register(StudentCourse)
admin.site.register(CourseSchool)
admin.site.register(SchoolAdmin)
admin.site.register(StudentSchool)
