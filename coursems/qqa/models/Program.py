from django.db import models
from qqa.models import Course

class Program(models.Model):
    # 课程类别
    学科基础 = "XKJC"
    专业必修 = "ZYBX"
    专业选修 = "ZYXX"
    全校共同课 = "QXGT"
    COURSE_TYPE = [
        (专业必修, "专业必修"),
        (专业选修, "专业选修"),
        (全校共同课, "全校共同课"),
        (学科基础, "学科基础")
    ]

    # 数据项定义
    program_no = models.CharField(max_length=12, primary_key=True)  # 
    course_type = models.CharField(max_length=6, choices=COURSE_TYPE)   # 课程类型
    course_no = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=10)

    # 功能
    def __str__(self): 
        return self.program_no

    # 元数据
    class Meta:
        app_label = 'qqa'
        db_table = 'Program'