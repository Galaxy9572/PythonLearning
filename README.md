># Python学习代码

### 1、Python代码格式规范

##### 1.1、变量名&函数名

###### 1.1.1、建议（不遵守不会报错，但都是Python官方的建议遵守）
- 全部都为小写
- 若有多个单词，则用下划线(_)分隔开

###### 1.1.2、强制（不遵守会报错）
- 不能以数字开头，否则会报错
- 不能有空格，否则会报错

正确示范：

```python
first_name = 'Saiya'
last_name = 'Li'
```

错误示范1：变量有空格
```python
first name = 'Saiya'
last name = 'Li'
```

错误示范2：不全为小写
```python
First_name = 'Saiya'
last_Name = 'Li'
```

错误示范3：以数字开头
```python
1first_name = 'Saiya'
2last_Name = 'Li'
```

##### 1.2、类名

###### 1.2.1、建议（不遵守不会报错，但都是Python官方的建议遵守）
- 如果是单个单词，那么首字母大写，其余小写
- 如果是多个单词，那么每个单词的首字母大写，其余小写
- 以上两点描述的书写风格即为驼峰（字母大小写间隔，像驼峰）

###### 1.2.2、强制（不遵守会报错）
- 不能以数字开头，否则会报错
- 不能有空格，否则会报错

正确示范：

```python
class Person:
    first_name = 'Saiya'
    last_name = 'Li'
```

错误示范1：有空格
```python
class Per son:
    first_name = 'Saiya'
    last_name = 'Li'
```

错误示范2：不是驼峰风格
```python
class person:
    first_name = 'Saiya'
    last_name = 'Li'
```

错误示范3：以数字开头
```python
class 1Person:
    first_name = 'Saiya'
    last_name = 'Li'
```