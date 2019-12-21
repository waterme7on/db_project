from django.contrib import admin
from .models.Course import Course
from .models.Student import Student
from .models.Teacher import Teacher

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
