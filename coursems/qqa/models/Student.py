from django.db import models

# Create your models here.
class Student(models.Model):
    sno = models.AutoField(primary_key=True)  # 主码：学生编号
    name = models.CharField(max_length=12)   #属性：学生姓名
    sex = models.CharField(max_length=6)    #性别
    age = models.IntegerField()         #年龄

    def __str__(self):
        return self.name
        
    class Meta:
        app_label = 'qqa'
        db_table = 'Student'