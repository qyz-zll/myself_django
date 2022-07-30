from django.db import models


class WangUser(models.Model):
    username = models.CharField(max_length=32, unique=True)  # 用户名
    password = models.CharField(max_length=32)  # 密码
    email = models.CharField(max_length=32)  # 邮箱

    # User object 是获取的数据,无法显示是以为没有对数据进行输出.
    # 在应用下的models.py 为创建的User类 设置 __str__ 魔方反法
    # __srt__ 在输入时自动触发
    # self.xxx  xxx是前面定义过的字段

    def __str__(self):
        return '%s %s' % (self.username, self.password)

class department(models.Model):
    dep_name=models.CharField(max_length=32,verbose_name='部门名称',unique=True,blank=False)
    dep_script=models.CharField(max_length=60,verbose_name='备注说明',null=True)
