from django.db import models
from qqa.models import Course

class Courlas(models.Model):
    # 数据项定义
    courlas_no = models.CharField(max_length=12, primary_key=True)  # 编号
    course_no = models.ForeignKey(Course, on_delete=models.CASCADE)
    term = models.DateField(verbose_name="学期")
    syllabus = models.CharField(max_length=15)  # 大纲（URL）
    time_location = models.CharField(max_length=120)
    selected_num = models.IntegerField(default=0)
    max_select_num = models.IntegerField(default=40)
    '''
        time_location: {
        "num" : xx，
        "info": [  
            {"time":[ 0,  1 ]   ,  "location": "教一"  }  ,  {“time”：[ 15，16 ] ,   "location": "教三"   },   ]， 
        }  
    '''
    
    # 功能
    def __str__(self): 
        return self.courlas_no    

    # 元数据
    class Meta:
        app_label = 'qqa'
        db_table = 'Courlas'