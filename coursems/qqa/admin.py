from django.contrib import admin
from .models.School import * 
from .models.Major import * 
from .models.Class import * 
from .models.Course import * 
from .models.Courlas import * 
from .models.Program import * 
from .models.Student import * 
from .models.Teacher import * 
from .models.ClassMajor import * 
from .models.SchoolAdmin import * 
from .models.StudentClass import * 
from .models.TeacherCourlas import * 
from .models.MajorProgram import * 
from .models.SelectRecord import * 
from .models.PartlyVisible import * 
from .models.StudentCourlas import * 
from .models.User import * 
from .models.Phase import * 


# Register your models here.
admin.site.register(Class)
admin.site.register(Program)
admin.site.register(Teacher)
admin.site.register(ClassMajor)
admin.site.register(School)
admin.site.register(TeacherCourlas)
admin.site.register(Courlas)
admin.site.register(SchoolAdmin)
admin.site.register(Course)
admin.site.register(SelectRecord)
admin.site.register(User)
admin.site.register(Major)
admin.site.register(Student)
admin.site.register(MajorProgram)
admin.site.register(StudentClass)
admin.site.register(PartlyVisible)
admin.site.register(StudentCourlas)
admin.site.register(Phase)