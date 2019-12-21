# -*- encode:utf-8 -*-

from django.db import models

class Teacher(models.Model):

    助理教授 = "Assitant"
    副教授 = "Associate"
    教授 = "Professor"
    讲师 = "Instructor"
    TITLE_TYPE = [
        (讲师,"讲师"),
        (助理教授,"助理教授"),
        (副教授,"副教授"),
        (教授,"教授")
   ]
    
    # 数据项定义
    teacher_no = models.AutoField(primary_key=True)  # 主码：教师编号
    teacher_name = models.CharField(max_length=20)   # 教师名字
    gender = models.CharField(max_length=2) # 性别
    title = models.CharField(max_length=15,choices=TITLE_TYPE, default = "Instructor") # 职称
    
    # __str__: 给出老师和职称
    def __str__(self): 
        return "name: "+ self.teacher_name +" title: "+self.title


    class Meta:
        app_label = 'qqa'
        db_table = 'Teacher'