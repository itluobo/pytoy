#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
# 解决方法为只要在文件开头加入 # -*- coding: UTF-8 -*- 或者 #coding=utf-8 就行了

# number
i = 5
print i
i = i + 1
print i
i = i + 0.5
print i
print str(i)

a = "Hello"
b = "Python"
 
print "a + b 输出结果：", a + b 
print "a * 2 输出结果：", a * 2 
print "a[1] 输出结果：", a[1] 
print "a[1:4] 输出结果：", a[1:4] 
 
if( "H" in a) :
    print "H 在变量 a 中" 
else :
    print "H 不在变量 a 中" 
 
if( "M" not in a) :
    print "M 不在变量 a 中" 
else :
    print "M 在变量 a 中"

# string
s = '''This is a multi-line string.
This is the second line.'''
print s

print s[1:9]
print s[10:]

# list
l = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
# print l               # 输出完整列表
print l[0]            # 输出列表的第一个元素
print l[1:3]          # 输出第二个至第三个元素 
l.append('Runoob')
print l[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print l + tinylist    # 打印组合的列表

# 元组 
# 元组是另一个数据类型，类似于List（列表）。
# 元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
 
print tuple               # 输出完整元组
print tuple[0]            # 输出元组的第一个元素
print tuple[1:3]          # 输出第二个至第三个的元素 
print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2       # 输出元组两次
print tuple + tinytuple   # 打印组合的元组

# map
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
 
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
 
 
print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值
for k, v in dict.items():
	print(k, v)