# -*- encode:utf-8 -*-

from django.db import models
import django.db.models.deletion

class Course(models.Model):
    
    # 变量定义
    # 课程类别
    专业必修 = "ZYBX"
    专业选修 = "ZYXX"
    COURSE_TYPE = [
        (专业必修, "专业必修"),
        (专业选修, "专业选修")
    ]
    
    # 数据项定义
    course_no = models.AutoField(primary_key=True)  # 主码：课程编号
    type = models.CharField(max_length=4, choices=COURSE_TYPE)  # 课程类型
    course_name = models.CharField(max_length=20)   # 课程名

    # 功能
    # __str__：得到课程名
    def __str__(self): 
        return self.course_name    

    # course_no = models.CharField(max_length=12, unique=True, primary_key=True)    # 主码

    # 元数据
    class Meta:
        app_label = 'qqa'
        db_table = 'Course'