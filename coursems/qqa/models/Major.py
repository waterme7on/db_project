from django.db import models
from qqa.models.School import *

class Major(models.Model):
    # 数据项定义
    major_no = models.CharField(max_length=12, primary_key=True)  # 编号
    major_name = models.CharField(max_length=20)   # 专业名
    school_no = models.ForeignKey(School, on_delete=models.CASCADE)
    

    # 功能
    def __str__(self): 
        return self.major_name    

    # 元数据
    class Meta:
        app_label = 'qqa'
        db_table = 'Major'