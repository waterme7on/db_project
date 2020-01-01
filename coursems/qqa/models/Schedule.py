from django.db import models

class Schedule(models.Model):
    
    # 数据项定义
    term = models.CharField(max_length=10)  # 年份春秋
    phase = models.IntegerField()   # 阶段
    beg_time = models.DateTimeField()  
    end_time = models.DateTimeField()   

    # 功能
    # __str__：得到学院名
    def __str__(self): 
        return self.term + str(self.phase)

    # 元数据
    class Meta:
        app_label = 'qqa'
        db_table = 'Phase'