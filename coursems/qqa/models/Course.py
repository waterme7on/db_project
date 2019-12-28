from django.db import models

class Course(models.Model):
    # course_no    course_name    credit    syllabus(URL)    is_partly_visible :0是全部公开
    # 数据项定义
    course_no = models.CharField(max_length=12, primary_key=True)  # 主码：课程编号
    course_name = models.CharField(max_length=20)   # 课程名
    credit = models.PositiveIntegerField()   # 学分
    syllabus = models.CharField(max_length=15)  # 大纲（URL）
    is_partly_visible = models.PositiveIntegerField()   #

    # 功能
    # __str__：得到课程名
    def __str__(self): 
        return self.course_name    

    # 元数据
    class Meta:
        app_label = 'qqa'
        db_table = 'Course'