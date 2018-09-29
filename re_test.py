#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 正则表达式

#导入re模块
import re

#返回pattern对象
# re.compile(string[,flag])  
# flag定义
# • re.I(全拼：IGNORECASE): 忽略大小写（括号内是完整写法，下同）
# • re.M(全拼：MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
# • re.S(全拼：DOTALL): 点任意匹配模式，改变'.'的行为
# • re.L(全拼：LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
# • re.U(全拼：UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
# • re.X(全拼：VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。

def hello_match():
	# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
	pattern = re.compile(r'hello')

	# 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
	result1 = re.match(pattern,'hello')
	result2 = re.match(pattern,'helloo hehe!')
	result3 = re.match(pattern,'helo hehe!')
	result4 = re.match(pattern,'hello hehe! hello hello')

	if result1:
	    print result1.group()
	else:
	    print '1匹配失败！'

	if result2:
	    print result2.group()
	else:
	    print '2匹配失败！'

	if result3:
	    print result3.group()
	else:
	    print '3匹配失败！'

	if result4:
	    print result4.group()
	else:
	    print '4匹配失败！'

# hello_match()

def hello_detail_match():
	# 匹配如下内容：单词+空格+单词+任意字符
	m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')

	print "m.string:", m.string
	print "m.re:", m.re
	print "m.pos:", m.pos
	print "m.endpos:", m.endpos
	print "m.lastindex:", m.lastindex
	print "m.lastgroup:", m.lastgroup
	print "m.group():", m.group()
	print "m.group(1):", m.group(1)
	print "m.group(1,2):", m.group(1, 2)
	print "m.groups():", m.groups()
	print "m.groupdict():", m.groupdict()
	print "m.start(2):", m.start(2)
	print "m.end(2):", m.end(2)
	print "m.span(2):", m.span(2)
	print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')

# hello_detail_match()

# search方法与match方法极其类似，区别在于match()函数只检测re是不是
# 在string的开始位置匹配，search()会扫描整个string查找匹配，
# match（）只有在0位置匹配成功的话才有返回，
# 如果不是开始位置匹配成功的话，match()就返回None。
# 同样，search方法的返回对象同样match()返回对象的方法和属性
def hello_search():
	# 将正则表达式编译成Pattern对象
	pattern = re.compile(r'world')
	# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
	# 这个例子中使用match()无法成功匹配
	match = re.search(pattern,'hello world!')
	if match:
	    # 使用Match获得分组信息
	    print match.group()

# hello_search()

# 按照能够匹配的子串将string分割后返回列表。
# maxsplit用于指定最大分割次数，不指定将全部分割
def hello_split():
	pattern = re.compile(r'\d+')
	print re.split(pattern,'one1two2three3four4')
	print re.split(pattern,'one1two2three3four4', 2)

# hello_split()

# 搜索string，以列表形式返回全部能匹配的子串
def hello_findall():
	pattern = re.compile(r'\d+')
	print re.findall(pattern,'one1two2three3four4')

# hello_findall()

# 搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器
def hello_finditer():
	pattern = re.compile(r'\d+')
	for m in re.finditer(pattern,'one1two2three3four4'):
	    print m.group(), "hehe"

# hello_finditer()

# re.sub(pattern, repl, string[, count])
# 使用repl替换string中每一个匹配的子串后返回替换后的字符串。
# 当repl是一个字符串时，可以使用\id或\g、\g引用分组，但不能使用编号0。
# 当repl是一个方法时，这个方法应当只接受一个参数（Match对象），
# 并返回一个字符串用于替换（返回的字符串中不能再引用分组）。
# count用于指定最多替换次数，不指定时全部替换。
def hello_sub():
	pattern = re.compile(r'(\w+) (\w+)')
	s = 'i say, hello world!'
	 
	print re.sub(pattern,r'\2 \1', s)
	 
	def func(m):
	    return m.group(1).title() + ' ' + m.group(2).title()
	 
	print re.sub(pattern,func, s)

# hello_sub()

# re.subn(pattern, repl, string[, count])
# 返回 (sub(repl, string[, count]), 替换次数)。
def hello_subn():
	pattern = re.compile(r'(\w+) (\w+)')
	s = 'i say, hello world!'
	 
	print re.subn(pattern,r'\2 \1', s)
	 
	def func(m):
	    return m.group(1).title() + ' ' + m.group(2).title()
	 
	a, b = re.subn(pattern,func, s)
	print b
	print a

# hello_subn()
