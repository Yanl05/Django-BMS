# 编写自定义filter
from django import template
register = template.Library()

# 告诉Django的模板语言，现在又一个自定义的方法名字叫sb
@register.filter(name="sb")
def add_sb(arg):
    return "{} sb".format(arg)

@register.filter(name="addstr")
def add_str(arg, arg2):
    """
    第一个参数是管道符前面的那个变量
    :param arg:管道符前面的变量
    :param arg2:冒号后面引号里面的变量
    :return:
    """
    return "{} {}".format(arg, arg2)