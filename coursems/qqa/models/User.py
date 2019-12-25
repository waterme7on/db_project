from django.db import models

# Create your models here.
class User(models.Model):

    学生 = "1"
    教师 = "2"
    教秘 = "3"
    character = [
        (学生, "学生"),
        (教师, "教师"),
        (教秘, "教秘"),
    ]
    #数据项定义
    account = models.CharField(max_length=20, primary_key=True)
    character = models.CharField(max_length=1, choices=character)
    x_no = models.CharField(max_length=12) # 对应的student_no 或 teacher_no 或 admin_no
    password = models.CharField(max_length=100, blank=True) #密文存储的密码

    # 功能
    # 得到账号
    def __str__(self):
        return self.account
        
    # 元数据
    class Meta:
        app_label = 'qqa'
        db_table = 'User'