from django.db import models

# Create your models here.
class Student(models.Model):

    #数据项定义
    student_no = models.AutoField(primary_key=True)  # 主码：学生编号
    student_name = models.CharField(max_length=12)   #属性：学生姓名
    student_sex = models.CharField(max_length=6)    #性别
    student_age = models.IntegerField()         #年龄


    # 功能
    # 得到学生名
    def __str__(self):
        return self.student_name
        
    # 元数据
    class Meta:
        app_label = 'qqa'
        db_table = 'Student'