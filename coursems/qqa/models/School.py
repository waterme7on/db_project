# -*- encode:utf-8 -*-

from django.db import models
import django.db.models.deletion

class School(models.Model):
    
    # 数据项定义
    school_no = models.CharField(max_length=12, primary_key=True)  # 主码：学院编号
    school_name = models.CharField(max_length=20)   # 学院名

    # 功能
    # __str__：得到学院名
    def __str__(self): 
        return self.school_name    

    # 元数据
    class Meta:
        app_label = 'qqa'
        db_table = 'School'