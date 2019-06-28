from django.contrib import admin
from index.models import User
# Register your models here.
#后台管理相关文件
# python manage.py createsuperuser 创建超级管理员用户

#注册模型类
admin.site.register(User)