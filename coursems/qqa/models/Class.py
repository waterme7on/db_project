from django.db import models
from qqa.models.Major import *

class Class(models.Model):
    # 数据项定义
    class_no = models.CharField(max_length=12, primary_key=True)  # 编号
    major_no = models.ForeignKey(Major, on_delete=models.CASCADE)
    enrollment_year = models.CharField(max_length=12, verbose_name="入学时间")

    # 功能
    def __str__(self): 
        return self.class_no    

    # 元数据
    class Meta:
        app_label = 'qqa'
        db_table = 'Class'