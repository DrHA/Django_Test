from django.db import models

# Create your models here.

#用户表
class UserInfo(models.Model):
    #自增列，一般做主键使用
    id = models.AutoField
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    email = models.EmailField(max_length=60,default="anwenjie@esunny.cc")

#服务器列表
class Server_list(models.Model):
    user = models.ForeignKey(UserInfo)
    IP = models.GenericIPAddressField(default="127.0.0.1")
    user = models.ForeignKey(UserInfo)
    pwd = models.CharField(max_length=128)
    update_time = models.DateField(auto_now=True)

#日志记录
class Log(models.Model):
    user = models.ForeignKey(UserInfo)
    #每次保存自动填写当前时间
    time = models.DateField(auto_now=True)
    content = models.TextField(null=True)

