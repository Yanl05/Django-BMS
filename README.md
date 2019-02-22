# Django-BMS
## 图书管理系统

* 三种角色：书籍、出版社、作者 <br>
>角色间的关系： <br>
>>出版社和书: 一对多    --> 外键 <br>
>>书和作者:   多对多    --> 用第三张表做关联 <br>
		
* ORM操作MySQL中的数据，对数据进行增删查改。 <br>

`涉及Django模板语言中的点：` <br>
>1.变量相关：{{ }} <br>
>2.逻辑相关：{% if|for %}
>3.filter
>>内置filter / 自定义filter
>4.母版和继承
>>base.html / {% extends 'base.html' %}
>5.组件
>>{% include 'xxx.html'%}
>6.静态文件的写法
	```html
		{% load static %}
		{% static 'jQuery-3.3.1.js' %}
		```html
		{# 常用名保存为简称 #} <br>
		{% load static %} <br>
		<img src="{% static '111.jpg' as xiaomao %}" alt=""> # 不显示 <br>
		<img src="{{ xiaomao }}" alt=""> <br>
		
>7.自定义simple_tag和inclusion_tag  <br>
>>simple_tag： 和自定义filter类似，可以接受更灵活的参数 <br>
>>inclusion_tag： 用于返回html代码片段 <br>
