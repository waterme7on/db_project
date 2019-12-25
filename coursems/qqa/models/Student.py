from django.db import models

# Create your models here.
class Student(models.Model):

    大一 = "1"
    大二 = "2"
    大三 = "3"
    大四 = "4"
    GRADE = [
        (大一, "大一"),
        (大二, "大二"),
        (大三, "大三"),
        (大四, "大四"),
    ]
    #数据项定义
    # student_no = models.AutoField(primary_key=True)  # 主码：学生编号
    student_no = models.CharField(max_length=12, primary_key=True)  # 主码：学生编号
    student_name = models.CharField(max_length=12)   #属性：学生姓名
    gender = models.CharField(max_length=6)    #性别
    age = models.IntegerField()         #年龄
    # grade = models.CharField(max_length=1,choices=GRADE, default=大一)
    password = models.CharField(max_length=20, blank=True)

    # 功能
    # 得到学生名
    def __str__(self):
        return self.student_name
        
    # 元数据
    class Meta:
        app_label = 'qqa'
        db_table = 'Student'