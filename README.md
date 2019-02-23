# Django-BMS
## 图书管理系统

* 三种角色：书籍、出版社、作者 <br>
>角色间的关系： <br>
>>出版社和书: 一对多    --> 外键 <br>
>>书和作者:   多对多    --> 用第三张表做关联 <br>
		
* ORM操作MySQL中的数据，对数据进行增删查改。 <br>

`涉及Django模板语言中的点：` <br>
>1.变量相关：{{ }} <br>
>2.逻辑相关：{% if|for %} <br>
>3.filter
>>内置filter / 自定义filter <br>

>4.母版和继承 <br>
>>base.html / {% extends 'base.html' %} <br>

>5.组件 <br>
>>{% include 'xxx.html'%} <br>

>6.静态文件的写法 <br>
```
{% load static %}
{% static 'jQuery-3.3.1.js' %}
```

```
{# 常用路径保存为一个变量 #}
{% load static %}
<img src="{% static '111.jpg' as xiaomao %}" alt=""> # 不显示
<img src="{{ xiaomao }}" alt="">
```

>7.自定义simple_tag和inclusion_tag  <br>
>>simple_tag： 和自定义filter类似，可以接受更灵活的参数 <br>
>>inclusion_tag： 用于返回html代码片段 <br>
