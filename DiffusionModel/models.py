from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    '''用户表'''
    # name = models.CharField(verbose_name='账号', max_length=32,default=None)
    username = models.CharField(verbose_name='账号', max_length=150, unique=True, default='')
    # password = models.CharField(verbose_name='密码', max_length=64,default=None)
    # age = models.IntegerField(verbose_name='年龄')
    #有约束 on_delete=models.CASCADE代表级联删除
    # depart = models.Foreignkey(to='表名',to_field='表中的列',null=True,blank=True,on_delete=models.CASCADE)



