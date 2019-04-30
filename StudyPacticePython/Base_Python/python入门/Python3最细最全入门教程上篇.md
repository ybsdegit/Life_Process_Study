
# python基础教程

## 引言

如何把以下这个不规则的列表 a 里的所有元素一个个写好，专业术语叫打平 (fatten)?


```python
a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
```


```python
"""
这一行代码，用到了迭代、匿名函数、递推函数、解析式这些技巧。
初学者一看只会说“好酷啊，但看不懂”，
看完本帖和下帖后，我保证你会说“我也会这样用了，真酷！”
"""
fn = lambda x: [y for l in x for y in fn(l)] if type(x) is list else [x]
fn(a)

```




    [1, 2, 3, 4, 5, 6, 7, 8]



## 1 基本数据类型
Python 里面有自己的内置数据类型 (build-in data type)，本节介绍基本的三种，分别是
* 整型 (int)，
* 浮点型 (float)，
* 布尔型 (bool)。


#### 整型


```python
a = 13214
print(a, type(a))
```

    13214 <class 'int'>
    

通过 print 的可看出 a 的值，以及类 (class) 是 int。Python 里面万物皆对象(object)，「整数」也不例外，只要是对象，就有相应的属性 (attributes) 和方法 (methods)。

* ### 知识点
通过 dir( X ) 和help( X ) 可看出 X 对应的对象里可用的属性和方法。

	* X 是 int，那么就是 int 的属性和方法
	* X 是 float，那么就是 float 的属性和方法等等


```python
dir(int)
```




    ['__abs__',
     '__add__',
     '__and__',
     '__bool__',
     '__ceil__',
     '__class__',
     '__delattr__',
     '__dir__',
     '__divmod__',
     '__doc__',
     '__eq__',
     '__float__',
     '__floor__',
     '__floordiv__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getnewargs__',
     '__gt__',
     '__hash__',
     '__index__',
     '__init__',
     '__init_subclass__',
     '__int__',
     '__invert__',
     '__le__',
     '__lshift__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__neg__',
     '__new__',
     '__or__',
     '__pos__',
     '__pow__',
     '__radd__',
     '__rand__',
     '__rdivmod__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rfloordiv__',
     '__rlshift__',
     '__rmod__',
     '__rmul__',
     '__ror__',
     '__round__',
     '__rpow__',
     '__rrshift__',
     '__rshift__',
     '__rsub__',
     '__rtruediv__',
     '__rxor__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__sub__',
     '__subclasshook__',
     '__truediv__',
     '__trunc__',
     '__xor__',
     'bit_length',
     'conjugate',
     'denominator',
     'from_bytes',
     'imag',
     'numerator',
     'real',
     'to_bytes']



'__xxx__': 可用方法
'xxx':    可用属性



```python
a.bit_length()
```




    14



该函数是找到一个整数的二进制表示，再返回其长度.

#### 浮点型

简单来说，浮点型 (float) 数就是实数， 例子如下：


print( 1, type(1) )
print( 1., type(1.) )

加一个小数点 . 就可以创建 float，不能再简单。
有时候我们想保留浮点型的小数点后 n 位。
可以用 decimal 包里的 Decimal 对象和 getcontext() 方法来实现。



```python
import decimal
from decimal import Decimal
"""
Python 里面有很多用途广泛的包 (package)，用什么你就引进 (import) 什么。
包也是对象，也可以用上面提到的dir(decimal) 来看其属性和方法。
比如 getcontext() 显示了 Decimal 对象的默认精度值是 28 位 (prec=28)，展示如下：
"""
```




    '\nPython 里面有很多用途广泛的包 (package)，用什么你就引进 (import) 什么。\n包也是对象，也可以用上面提到的dir(decimal) 来看其属性和方法。\n比如 getcontext() 显示了 Decimal 对象的默认精度值是 28 位 (prec=28)，展示如下：\n'




```python
decimal.getcontext()
```




    Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[Inexact, Rounded], traps=[InvalidOperation, DivisionByZero, Overflow])




```python
# 1/3 保留28位
d = Decimal(1) / Decimal(3)
d
```




    Decimal('0.3333333333333333333333333333')



那保留 4 位呢？用 getcontext().prec 来调整精度哦。


```python
decimal.getcontext().prec = 4
e = Decimal(1) / Decimal(3)
e
```




    Decimal('0.3333')



高精度的 float 加上低精度的 float，保持了高精度。


```python
0.3333333333333333333333333333 + 0.3333
```




    0.6666333333333333



#### 布尔型
布尔 (boolean) 型变量只能取两个值，True 和 False。当把布尔变量用在数字运算中，用 1 和 0 代表 True 和 False。



```python
T = True
F = False
print(T + 2)
print(F - 8)
```

    3
    -8
    


```python
# 基本类型
print( type(0), bool(0), bool(1) )
print( type(10.31), bool(0.00), bool(10.31) )
print( type(True), bool(False), bool(True) )
```

    <class 'int'> False True
    <class 'float'> False True
    <class 'bool'> False True
    

bool 作用在基本类型变量的总结：X 只要不是整型 0、浮点型 0.0，bool(X) 就是 True，其余就是 False。


```python
# 容器类型
print( type(''), bool( '' ), bool( 'python' ) )
print( type(()), bool( () ), bool( (10,) ) )
print( type([]), bool( [] ), bool( [1,2] ) )
print( type({}), bool( {} ), bool( {'a':1, 'b':2} ) )
print( type(set()), bool( set() ), bool( {1,2} ) )
```

    <class 'str'> False True
    <class 'tuple'> False True
    <class 'list'> False True
    <class 'dict'> False True
    <class 'set'> False True
    

bool 作用在容器类型变量的总结：X 只要不是空的变量，bool(X) 就是 True，其余就是 False。

确定bool(X) 的值是 True 还是 False，就看 X 是不是空，空的话就是 False，不空的话就是 True。

	* 对于数值变量，0, 0.0 都可认为是空的。
	* 对于容器变量，里面没元素就是空的。



此外两个布尔变量 P 和 Q 的逻辑运算的结果总结如下表：
![image.png](attachment:image.png)

## 容器数据类型
上节介绍的整型、浮点型和布尔型都可以看成是单独数据，而这些数据都可以放在一个容器里得到一个「容器类型」的数据，比如：

	* 字符 (str) 是一容器的字节 char，注意 Python 里面没有 char 类型的数据，可以把单字符的 str 当做 char。

	* 元组 (tuple)、列表 (list)、字典 (dict) 和集合 (set) 是一容器的任何类型变量。




#### 字符：
字符用于处理文本 (text) 数据，用「单引号 ’」和「双引号 “」来定义都可以。


```python
# 创建字符
t1 = 'i love coding'
print(t1, type(t1))

t2 = "I love coding"
print(t2, type(t2))
```

    i love coding <class 'str'>
    I love coding <class 'str'>
    

字符中常见的内置方法 (可以用 dir(str) 来查) 有

	* capitalize()：大写句首的字母
	* split()：把句子分成单词
	* find(x)：找到给定词 x 在句中的索引，找不到返回 -1
	* replace(x, y)：把句中 x 替代成 y
	* strip(x)：删除句首或句末含 x 的部分





```python
t1.capitalize()
```




    'I love coding'




```python
t2.split()
```




    ['I', 'love', 'coding']




```python
print(t1.find('love'))
print(t2.find('like'))
```

    2
    -1
    


```python
t2.replace('love', 'hate')
```




    'I hate coding'




```python
print( 'http://www.python.org'.strip('htp:/') )
print( 'http://www.python.org'.strip('.org') )
```

    www.python.org
    http://www.python
    

#### 索引和切片


```python
s = 'Python'
print( s )
print( s[2:4] )
print( s[-5:-2] )
print( s[2] )
print( s[-1] )
```

    Python
    th
    yth
    t
    n
    

知识点
Python 里面索引有三个特点 (经常让人困惑)：

	1. 从 0 开始 (和 C 一样)，不像 Matlab 从 1 开始。

	2. 切片通常写成 start:end 这种形式，包括「start 索引」对应的元素，不包括「end索引」对应的元素。因此 s[2:4] 只获取字符串第 3 个到第 4 个元素。

	3. 索引值可正可负，正索引从 0 开始，从左往右；负索引从 -1 开始，从右往左。使用负数索引时，会从最后一个元素开始计数。最后一个元素的位置编号是 -1。


这些特点引起读者对切片得到什么样的元素感到困惑。有个小窍门可以帮助大家快速锁定切片的元素，如下图。

![image.png](attachment:image.png)

与其把注意力放在元素对应的索引，不如想象将元素分开的隔栏，显然 6 个元素需要 7 个隔栏，隔栏索引也是从 0 开始，这样再看到 start:end 就认为是隔栏索引，那么获取的元素就是「隔栏 start」和「隔栏 end」之间包含的元素。如上图：

	* string[2:4] 就是「隔栏 2」和「隔栏 4」之间包含的元素，即 th
	* string[-5:-2] 就是「隔栏 -5」和「隔栏 -2」之间包含的元素，即 yth



正则表达式
正则表达式 (regular expression) 主要用于识别字符串中符合某种模式的部分，什么叫模式呢？用下面一个具体例子来讲解。


```python
input = """
'06/18/2019 13:00:00', 100, '1st';
'06/18/2019 13:30:00', 110, '2nd';
'06/18/2019 14:00:00', 120, '3rd'
"""
input
```




    "\n'06/18/2019 13:00:00', 100, '1st';\n'06/18/2019 13:30:00', 110, '2nd';\n'06/18/2019 14:00:00', 120, '3rd'\n"



假如你想把上面字符串中的「时间」的模式来抽象的表示出来，对照着具体表达式 '06/18/201913:00:00' 来看，我们发现该字符串有以下规则：

	1. 开头和结束都有个单引号 '
	2. 里面有多个 0-9 数字
	3. 里面有多个正斜线 / 和分号 : 
	4. 还有一个空格

因此我们用下面这样的模式


```python
import re
pattern = re.compile("'[0-9/:\s]+'")
```

再看这个抽象模式表达式 '[0-9/:\s]+'，里面符号的意思如下：

	* 最外面的两个单引号 ' 代表该模式以它们开始和结束
	* 中括号 [] 用来概括该模式涵盖的所有类型的字节
	* 0-9 代表数字类的字节
	* / 代表正斜线
	* : 代表分号
	* \s 代表空格
	* [] 外面的加号 + 代表 [] 里面的字节出现至少 1 次

有了模式 pattern，我们来看看是否能把字符串中所有符合 pattern 的日期表达式都找出来。


```python
pattern.findall(input)
```




    ["'06/18/2019 13:00:00'", "'06/18/2019 13:30:00'", "'06/18/2019 14:00:00'"]



结果是对的，之后你想怎么盘它就是你自己的事了，比如把 / 换成 -，比如用 datetime 里面的 striptime() 把日期里年、月、日、小时、分钟和秒都获取出来。

元组

#### 创建元组

「元组」定义语法为 

(元素1, 元素2, ..., 元素n)

关键点是「小括号 ()」和「逗号 ,」

	* 小括号把所有元素绑在一起
	* 逗号将每个元素一一分开

创建元组的例子如下：


```python
t1 = (1, 10.31, 'python')
t2 = 1, 10.31, 'python'
print( t1, type(t1) )
print( t2, type(t2) )
```

    (1, 10.31, 'python') <class 'tuple'>
    (1, 10.31, 'python') <class 'tuple'>
    

知识点
创建元组可以用小括号 ()，也可以什么都不用，为了可读性，建议还是用 ()。此外对于含单个元素的元组，务必记住要多加一个逗号，举例如下：


```python
print( type( ('OK') ) )  # 没有逗号 , 
print( type( ('OK',) ) ) # 有逗号 ,
```

    <class 'str'>
    <class 'tuple'>
    

看，没加逗号来创建含单元素的元组，Python 认为它是字符。

当然也可以创建二维元组：


```python
nested = (1, 10.31, 'python'), ('data', 11)
nested
```




    ((1, 10.31, 'python'), ('data', 11))



#### 索引和切片
元组中可以用整数来对它进行索引 (indexing) 和切片 (slicing)，不严谨的讲，前者是获取单个元素，后者是获取一组元素。接着上面二维元组的例子，先看看索引的代码：



```python
nested[0]
print( nested[0][0], nested[0][1], nested[0][2] )
```

    1 10.31 python
    

再看看切片的代码：


```python
nested[0][0:2] 
```




    (1, 10.31)



不可更改

元组有不可更改 (immutable) 的性质，因此不能直接给元组的元素赋值，例子如下 (注意「元组不支持元素赋值」的报错提示)。


```python
t = ('OK', [1, 2], True)
t[2] = False
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-22-2391723ab1a0> in <module>
          1 t = ('OK', [1, 2], True)
    ----> 2 t[2] = False
    

    TypeError: 'tuple' object does not support item assignment


但是只要元组中的元素可更改 (mutable)，那么我们可以直接更改其元素，注意这跟赋值其元素不同。如下例 t[1] 是列表，其内容可以更改，因此用 append 在列表后加一个值没问题。


```python
t[1].append(3)
t
```




    ('OK', [1, 2, 3, 3, 3], True)



内置方法

元组大小和内容都不可更改，因此只有 count 和 index 两种方法。


```python
t = (1, 10.31, 'python')
print( t.count('python') )
print( t.index(10.31) )
```

    1
    1
    

这两个方法返回值都是 1，但意思完全不同

	* count('python') 是记录在元组 t 中该元素出现几次，显然是 1 次
	* index(10.31) 是找到该元素在元组 t 的索引，显然是 1


#### 元组拼接

元组拼接 (concatenate) 有两种方式，用「加号 +」和「乘号 *」，前者首尾拼接，后者复制拼接。


```python
(1, 10.31, 'python') + ('data', 11) + ('OK',)
# (1, 10.31, 'python') * 2
```




    (1, 10.31, 'python', 'data', 11, 'OK')



#### 解压元组

解压 (unpack) 一维元组 (有几个元素左边括号定义几个变量）


```python
t = (1, 10.31, 'python')
(a, b, c) = t
print( a, b, c )
```

    1 10.31 python
    

解压二维元组 (按照元组里的元组结构来定义变量）


```python
t = (1, 10.31, ('OK','python'))
(a, b, (c,d)) = t
print( a, b, c, d )
```

    1 10.31 OK python
    

如果你只想要元组其中几个元素，用通配符「*」，英文叫 wildcard，在计算机语言中代表一个或多个元素。下例就是把多个元素丢给了 rest 变量。


```python
t = 1, 2, 3, 4, 5
a, b, *rest, c = t
print( a, b, c )
print( rest )
```

    1 2 5
    [3, 4]
    

如果你根本不在乎 rest 变量，那么就用通配符「*」加上下划线「_」，例子如下：


```python
a, b, *_ = t
print( a, b )
```

    1 2
    

#### 优点缺点

* 优点：占内存小，安全，创建遍历速度比列表快，可一赋多值。

* 缺点：不能添加和更改元素。

等等等，这里有点矛盾，元组的不可更改性即使优点 (安全) 有时缺点？确实是这样的，安全就没那么灵活，灵活就没那么安全。看看大佬廖雪峰怎么评价「不可更改性」吧


```python
import timeit
%timeit [1, 2, 3, 4, 5]
%timeit (1, 2, 3, 4, 5)
```

    44.5 ns ± 0.0824 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
    6.5 ns ± 0.00444 ns per loop (mean ± std. dev. of 7 runs, 100000000 loops each)
    

##### 遍历



```python
lst = [i for i in range(63335)]
tup = tuple(i for i in range(63335))
%timeit for each in lst: pass
%timeit for each in tup:pass
```

    405 µs ± 2.01 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    444 µs ± 1.57 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    

##### 占空间


```python
from sys import getsizeof
print(getsizeof(lst))
print(getsizeof(tup))
```

    514568
    506728
    

* 列表比元组稍微废点内存空间。

#### 列表
##### 创建列表
「列表」定义语法为 

            [元素1, 元素2, ..., 元素n]

关键点是「中括号 []」和「逗号 ,」

	* 中括号把所有元素绑在一起
	* 逗号将每个元素一一分开
创建列表的例子如下：


```python
l = [1, 10.31,'python']
print(l, type(l))
```

    [1, 10.31, 'python'] <class 'list'>
    

##### 内置方法
不像元组，列表内容可更改 (mutable)，因此附加 (append, extend)、插入 (insert)、删除 (remove, pop) 这些操作都可以用在它身上。

* 附加


```python
l.append([4, 3])
print(l)
l.extend([1.5, 2.0, 'ok'])
print(l)
```

    [1, 10.31, 'python', [4, 3], [4, 3], 1.5, 2.0, 'ok', [4, 3]]
    [1, 10.31, 'python', [4, 3], [4, 3], 1.5, 2.0, 'ok', [4, 3], 1.5, 2.0, 'ok']
    

严格来说 append 是追加，把一个东西整体添加在列表后，而 extend 是扩展，把一个东西里的所有元素添加在列表后。对着上面结果感受一下区别。



* 插入

insert(i, x) 在编号 i 位置前插入 x。对着下面结果感受一下。


```python
l.insert(1, 'abc') # insert object before the index position
l
```




    [1,
     'abc',
     'abc',
     'abc',
     'abc',
     10.31,
     'python',
     [4, 3],
     [4, 3],
     1.5,
     2.0,
     'ok',
     [4, 3],
     1.5,
     2.0,
     'ok']



* 删除

remove 和 pop 都可以删除元素

	* 前者是指定具体要删除的元素，比如 'python'
	* 后者是指定一个编号位置，比如 3，删除 l[3] 并返回出来



对着下面结果感受一下，具体用哪个看你需求。


```python
l.remove('ok') # remove first occurrence of object
l
```




    [1,
     'abc',
     'abc',
     'abc',
     'abc',
     10.31,
     [4, 3],
     [4, 3],
     1.5,
     2.0,
     [4, 3],
     1.5,
     2.0]




```python
p = l.pop(3) # removes and returns object at index. Only only pop 1 index position at any time.
print( p )
print( l ) 
```

    abc
    [1, 'abc', 'abc', 'abc', 10.31, [4, 3], [4, 3], 1.5, 2.0, [4, 3], 1.5, 2.0]
    

#### 切片索引

索引 (indexing) 和切片 (slicing) 语法在元组那节都讲了，而且怎么判断切片出来的元素在字符那节也讲了，规则如下图：
![image.png](attachment:image.png)
对照上图看下面两个例子 (顺着数和倒着数编号)：


```python
l = [7, 2, 9, 10, 1, 3, 7, 2, 0, 1]
l[1:5]
```




    [2, 9, 10, 1]




```python
l[-4:]
```




    [7, 2, 0, 1]




```python
# 列表可更改，因此可以用切片来赋值。
l[2:4] = [999, 1000]
l
```




    [7, 2, 999, 1000, 1, 3, 7, 2, 0, 1]



切片的通用写法是

start : stop : step

这三个在特定情况下都可以省去，我们来看看四种情况：



情况 1 - start : 以 step 为 1 (默认) 从编号 start 往列表尾部切片。


```python
print( l )
print( l[3:] )
print( l[-4:] )
print(l[:-1])
```

    [7, 2, 999, 1000, 1, 3, 7, 2, 0, 1]
    [1000, 1, 3, 7, 2, 0, 1]
    [7, 2, 0, 1]
    [7, 2, 999, 1000, 1, 3, 7, 2, 0]
    

情况 2 - : stop :以  step 为 1 (默认) 从列表头部往编号 stop 切片。


```python
print( l )
print( l[:6] )
print( l[:-4] )
```

    [7, 2, 999, 1000, 1, 3, 7, 2, 0, 1]
    [7, 2, 999, 1000, 1, 3]
    [7, 2, 999, 1000, 1, 3]
    

情况 3 - start : stop  以 step 为 1 (默认) 从编号 start 往编号 stop 切片。


```python
print( l )
print( l[2:4] )
print( l[-5:-1] )
```

    [7, 2, 999, 1000, 1, 3, 7, 2, 0, 1]
    [999, 1000]
    [3, 7, 2, 0]
    

情况 4 - start : stop : step  
以具体的 step 从编号 start 往编号 stop 切片。注意最后把 step 设为 -1，相当于将列表反向排列。


```python
print( l )
print( l[1:5:2] )
print( l[:5:2] )
print( l[1::2] )
print( l[::2] )
print( l[::-1] )
```

    [7, 2, 999, 1000, 1, 3, 7, 2, 0, 1]
    [2, 1000]
    [7, 999, 1]
    [2, 1000, 3, 2, 1]
    [7, 999, 1, 7, 0]
    [1, 0, 2, 7, 3, 1, 1000, 999, 2, 7]
    

##### 列表拼接
和元组拼接一样， 列表拼接也有两种方式，用「加号 +」和「乘号 *」，前者首尾拼接，后者复制拼接。



```python
[1, 10.31, 'python'] + ['data', 11] + ['OK']
[1, 10.31, 'python'] * 2
```




    [1, 10.31, 'python', 1, 10.31, 'python']



优点缺点
* 优点：灵活好用，可索引、可切片、可更改、可附加、可插入、可删除。

* 缺点：相比 tuple 创建和遍历速度慢，占内存。此外查找和插入时间较慢。

### 字典

#### 创建字典
「字典」定义语法为 

{元素1, 元素2, ..., 元素n}

其中每一个元素是一个「键值对」- 键:值 (key:value)

关键点是「大括号 {}」,「逗号 ,」和「冒号 :」

	* 大括号把所有元素绑在一起
	* 逗号将每个键值对一一分开
	* 冒号将键和值分开

创建字典的例子如下：


```python
d = {'Name' : 'Tencent',
     'Country' : 'China',
     'Industry' : 'Technology',
     'Code': '00700.HK',
     'Price' : '361 HKD'}
print(d, type(d))
```

    {'Name': 'Tencent', 'Country': 'China', 'Industry': 'Technology', 'Code': '00700.HK', 'Price': '361 HKD'} <class 'dict'>
    

#### 内置方法
字典里最常用的三个内置方法就是 keys(), values() 和 items()，分别是获取字典的键、值、对。


```python
print(list(d.keys()))
print(list(d.values()))
print(d.items())
```

    ['Name', 'Country', 'Industry', 'Code', 'Price']
    ['Tencent', 'China', 'Technology', '00700.HK', '361 HKD']
    dict_items([('Name', 'Tencent'), ('Country', 'China'), ('Industry', 'Technology'), ('Code', '00700.HK'), ('Price', '361 HKD')])
    

此外在字典上也有添加、获取、更新、删除等操作。



* 添加

比如加一个「总部：深圳」


```python
d['headquarter'] = 'shenzhen'
d
```




    {'Name': 'Tencent',
     'Country': 'China',
     'Industry': 'Technology',
     'Code': '00700.HK',
     'Price': '361 HKD',
     'headquarter': 'shenzhen'}



* 获取

比如想看看腾讯的股价是多少 (两种方法都可以)


```python
print(d['Price'])
print(d.get('Price'))
```

    361 HKD
    361 HKD
    

* 更新

比如更新腾讯的股价到 359 港币


```python
d['Price'] = '359 HKD'
d
```




    {'Name': 'Tencent',
     'Country': 'China',
     'Industry': 'Technology',
     'Code': '00700.HK',
     'Price': '359 HKD',
     'headquarter': 'shenzhen'}



* 删除

比如去掉股票代码 (code)


```python
del d['Code']
d

```




    {'Name': 'Tencent',
     'Country': 'China',
     'Industry': 'Technology',
     'Price': '359 HKD',
     'headquarter': 'shenzhen'}



或像列表里的 pop() 函数，删除行业 (industry) 并返回出来。


```python
print(d.pop('Industry'))
d
```

    Technology
    




    {'Name': 'Tencent',
     'Country': 'China',
     'Price': '359 HKD',
     'headquarter': 'shenzhen'}



#### 不可更改键
字典里的键是不可更改的，因此只有那些不可更改的数据类型才能当键，比如整数 (虽然怪怪的)、浮点数 (虽然怪怪的)、布尔 (虽然怪怪的)、字符、元组 (虽然怪怪的)，而列表却不行，因为它可更改。看个例子


```python
d = {2 : 'integer key',
     10.31 : 'float key',
     True : 'boolean key',
     ('OK',3) : 'tuple key'}
d
```




    {2: 'integer key',
     10.31: 'float key',
     True: 'boolean key',
     ('OK', 3): 'tuple key'}




虽然怪怪的，但这些 2, 10.31, True, ('OK', 3) 确实能当键。有个地方要注意下，True 其实和整数 1 是一样的，由于键不能重复，当你把 2 该成 1时，你会发现字典只会取其中一个键

那么如何快速判断一个数据类型 X 是不是可更改的呢？两种方法：

	1. 麻烦方法：用 id(X) 函数，对 X 进行某种操作，比较操作前后的 id，如果不一样，则 X 不可更改，如果一样，则 X 可更改。
	2. 便捷方法：用 hash(X)，只要不报错，证明 X 可被哈希，即不可更改，反过来不可被哈希，即可更改。

先看用 id() 函数的在整数 i 和列表 l 上的运行结果：


```python
i = 1
print( id(i) )
i = i + 2
print( id(i) )
```

    140732850594448
    140732850594512
    


```python
l = [1, 2]
print( id(l) )
l.append('Python')
print( id(l) )
```

    3026082498824
    3026082498824
    

用 hash() 函数的在字符 s，元组 t 和列表 l 上的运行结果：


```python
hash('Name')
```




    -5122428430537815772




```python
hash( (1,2,'Python') )
```




    8941961007093465794




```python
hash( [1,2,'Python'] )
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-132-54c2881f2699> in <module>
    ----> 1 hash( [1,2,'Python'] )
    

    TypeError: unhashable type: 'list'


字符 s 和元组 t 都能被哈希，因此它们是不可更改的。列表 l 不能被哈希，因此它是可更改的。

##### 优点缺点
优点：查找和插入速度快
缺点：占内存大

### 集合
#### 创建集合 
「集合」有两种定义语法，
第一种是

    {元素1, 元素2, ..., 元素n}

关键点是「大括号 {}」和「逗号 ,」

	* 大括号把所有元素绑在一起
	* 逗号将每个元素一一分开

第二种是
    用 set() 函数，把列表或元组转换成集合。

##### set( 列表 或 元组 )
创建集合的例子如下 (用两者方法创建 A 和 B)：

从 A 的结果发现集合的两个特点：无序 (unordered) 和唯一 (unique)。由于 set 存储的是无序集合，所以我们没法通过索引来访问，但是可以判断一个元素是否在集合中。


```python
A = set(['u', 'd', 'ud', 'du', 'd', 'du'])
B = {'d', 'dd', 'uu', 'u'}
print( A )
print( B )
```

    {'d', 'du', 'ud', 'u'}
    {'d', 'uu', 'dd', 'u'}
    


```python
B[1]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-135-ee721d8948fe> in <module>
    ----> 1 B[1]
    

    TypeError: 'set' object is not subscriptable



```python
'u' in B

```




    True



##### 内置方法
用 set 的内置方法就把它当成是数学上的集，那么并集、交集、差集都可以玩通了。

###### 并集OR



```python
print( A.union(B) ) # All unique elements in A or B
print( A | B ) # A OR B
```

    {'dd', 'du', 'd', 'u', 'uu', 'ud'}
    {'dd', 'du', 'd', 'u', 'uu', 'ud'}
    

###### 交集AND


```python
print(A.intersection(B))  # All elements in both A and B
print(A & B)  # A and B
```

    {'d', 'u'}
    {'d', 'u'}
    

###### 差集A-B


```python
print(A.difference(B))  # Elements in A but not in B
print(B - A) # B minus A 

```

    {'du', 'ud'}
    {'uu', 'dd'}
    

##### 对称差集 XOR


```python
print(A.symmetric_difference(B)) # All elements in either A or B ,but not both
print(A ^ B)
```

    {'du', 'dd', 'uu', 'ud'}
    {'du', 'dd', 'uu', 'ud'}
    

##### * 优点缺点
* 优点：不用判断重复的元素
* 缺点：不能存储可变对象

你看集合的「唯一」特性还不是双刃剑，既可以是优点，又可以是缺点，所有东西都有 trade-off 的，要不然它就没有存在的必要了。

## 3. 条件语句 & 迭代循环
在编写程序时，我们要

	* 在不同条件下完成不同动作，条件语句 (conditional statement) 赋予程序这种能力。



	* 重复的完成某些动作，迭代循环 (iterative loop) 赋予程序这种能力。

#### 条件语句
条件语句太简单了，大体有四种格式

	1. if 语句
	2. if-else 语句
	3. if-elif-else 语句
	4. nested 语句
看了下面四幅图 (包含代码) 应该秒懂条件语句，其实任何会说话的人都应该懂它。


* if
![image.png](attachment:image.png)
if x > 0:    
    print( 'x is positive' )
   
   
* if-else
![image.png](attachment:image.png)
if x % 2 == 0:
    print( 'x is even' )
else :
    print( 'x is odd' )
    
    
* if-elif-else 
![image.png](attachment:image.png)
if x < y:
    print( 'x is less than y' )
elif x > y:
    print( 'x is greater than y' )
else:
    print( 'x and y are equal' )
  给定多元条件，满足条件 1 做事 A1，满足条件 2 做事 A2，..., 满足条件 n 做事 An。直到把所有条件遍历完。
  
  
* Nested if
![image.png](attachment:image.png)
if x == y:
    print( 'x and y are equal' )
else:
    if x < y:
        print( 'x is less than y' )
    else:
        print( 'x is greater than y' )
给定多元条件，满足条件 1 做事 A1，不满足就

    给定多元条件，满足条件 2 做事 A2，不满足就

        ...

直到把所有条件遍历完。

#### 迭代循环
对于迭代循环，Python 里面有「while 循环」和「for 循环」，没有「do-while 循环」。

* **while 循环**

While 循环非常简单，做事直到 while 后面的语句为 False。上例就是打印从 n (初始值为 5) 一直到 1，循环执行了 5 次。

一般来说，在 「while 循环」中，迭代的次数事先是不知道的，因为通常你不知道 while 后面的语句从 True 变成 False了。


```python
n =5
while n > 0:
    print(n)
    n = n-1
print('learned')
```

    5
    4
    3
    2
    1
    learned
    

* **for 循环**

更多时候我们希望事先直到循环的次数，比如在列表、元组、字典等容器类数据上遍历一遍，在每个元素层面上做点事情。这时候就需要「for 循环」了。


```python
languages = ['Python', 'R', 'Matlab', 'C++', 'java']
for language in languages:
    print('learning ', language)
print('learned')
```

    learning  Python
    learning  R
    learning  Matlab
    learning  C++
    learning  java
    learned
    

最后介绍一个稍微有点特殊的函数 enumerate()，和 for loop 一起用的语法如下

    for i, a in enumerate(A)
        do something with a  

发现区别了没？用 enumerate(A) 不仅返回了 A 中的元素，还顺便给该元素一个索引值 (默认从 0 开始)。此外，用 enumerate(A, j) 还可以确定索引起始值为 j。看下面例子。


```python
languages = ['Python', 'R', 'Matlab', 'C++', 'java']
for i, language in enumerate(languages, 1):
    print(i, 'learning', language)
print('learned')
```

    1 learning Python
    2 learning R
    3 learning Matlab
    4 learning C++
    5 learning java
    learned
    

## 总结
学习任何一种都要从最基本开始，基本的东西无外乎数据类型、条件语句和递推循环。

数据类型分两种：

	* 单独类型：整型、浮点型、布尔型
	* 容器类型：字符、元组、列表、字典、集合

按照 Python 里「万物皆对象」的思路，学习每一个对象里面的属性 (attributes) 和方法 (methods)，你不需要记住所有，有个大概印象有哪些，通过 dir() 来锁定具体表达式，再去官网上查询所有细节。这么学真的很系统而简单。此外学的时候一定要带着“它的优缺点是什么”这样的问题，所有东西都有 trade-off，一个满身都是缺点的东西就没有存在的必要，既然存在肯定有可取之处。


条件语句 (if, if-else, if-elif-else, nested if) 是为了在不同条件下执行不同操作，而迭代循环 (while, for) 是重复的完成相同操作。

抓住上面大框架，最好还要以目标导向 (我学 python 就是为了搞自动化躺着赚钱)，别管这目标难度如何，起码可以保证我累得时候还鸡血满满不会轻言放弃。这样我就足够主动的去学一样东西并学精学深，目标越难完成，我主动性就越强。

之后所有的细节都可以慢慢来，虽然我觉得本篇已经挖了不少细节了，像 hashability，但肯定还有更多等着去挖，半篇帖子就想覆盖 Python 所有内容不是开玩笑吗？但**抓住大框架，有目标导向，对有效学习任何内容都适用。**
