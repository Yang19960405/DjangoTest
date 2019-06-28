from django.db import models

# Create your models here.


class User(models.Model):
    """
    ORM框架  可以根据实体映射表 首先要继承models.Model
    创建实体时不需要创建ID  会默认自动创建
    """

    #CharField表示字符串类型  max_length定义最大长度
    user_name=models.CharField(max_length=100)
    user_pass=models.CharField(max_length=100)
    user_number=models.CharField(max_length=11)
    user_update=models.DateField()
    user_rode=models.ForeignKey('Rode')

    #执行命令 python manage.py migrations 生成迁移文件
    #执行命令 python manage.py migrate 执行迁移生成表
    pass

class Rode(models.Model):
    rode_name=models.CharField(max_length=20)
    pass

