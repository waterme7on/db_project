from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class User(models.Model):

    学生 = "student"
    教师 = "teacher"
    教秘 = "admin"
    管理员 = "superadmin"
    character = [
        (学生, "学生"),
        (教师, "教师"),
        (教秘, "教秘"),
        (管理员, "管理员"),
    ]
    #数据项定义
    account = models.CharField(max_length=30, primary_key=True)
    character = models.CharField(max_length=12, choices=character)
    x_no = models.CharField(max_length=12) # 对应的student_no 或 teacher_no 或 admin_no
    password = models.CharField(max_length=100, blank=True) #密文存储的密码

    # 功能
    # 得到账号
    def __str__(self):
        return self.account

    # 重写save, 在保存密码时加密存储
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    # 元数据
    class Meta:
        app_label = 'qqa'
        db_table = 'User'