from django import template

register = template.Library()

@register.simple_tag(name="mysum")
def my_sum(arg1, arg2, arg3):
    return "{} + {} + {}".format(arg1, arg2, arg3)

@register.inclusion_tag('result.html')
def show_result(n):
    n = 1 if n < 1 else int(n)
    data = ["第{}项".format(i) for i in range(1, n+1)]
    return {'data': data}
