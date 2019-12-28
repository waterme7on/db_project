from django.contrib import admin
from .models.Course import Course
from .models.Student import Student
from .models.Teacher import Teacher
from .models.School import School
from .models.TeacherCourlas import TeacherCourlas
from .models.StudentCourlas import StudentCourlas
from .models.SchoolAdmin import SchoolAdmin
from .models.User import User

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(School)
admin.site.register(User)
admin.site.register(TeacherCourlas)
admin.site.register(StudentCourlas)
admin.site.register(SchoolAdmin)
