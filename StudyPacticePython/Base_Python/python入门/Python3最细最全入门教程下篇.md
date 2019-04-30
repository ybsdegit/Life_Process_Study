
>接着上篇继续后面两个章节，函数和解析式。
![image.png](attachment:image.png)

## 4. 函数
Python 里函数太重要了 (每种语言都很重要)。函数的通用好处就不用多说了吧，重复使用代码，增强代码可读性等等。

还记得 Python 里面『万物皆对象』么？Python 把函数也当成对象，可以从另一个函数中返回出来而去构建高阶函数，比如

	* 参数是函数 
	* 返回值是函数



### 正规函数
Python 里面的正规函数 (normal function) 就像其他语言的函数一样，之所以说正规函数是因为还有些「不正规」的，比如**匿名函数，高阶函数**等等。

但即便是正规函数，Python 的函数具有非常灵活多样的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。从简到繁的参数形态如下：

	1. 位置参数 (positional argument)
	2. 默认参数 (default argument)
	3. 可变参数 (variable argument)
	4. 关键字参数 (keyword argument)
	5. 命名关键字参数 (name keyword argument)
	6. 参数组合

每种参数形态都有自己对应的应用，接下来用定义一个金融产品为例来说明各种参数形态的具体用法。

先从最简单的「位置参数」开始介绍：
#### 位置参数
![image.png](attachment:image.png)
解释一下函数里面的各个部分：

	* def - 定义正规函数要写 def 关键词。
	* function_name - 函数名，起名最好有意义。
	* arg1 - 位置参数 ，这些参数在调用函数 (call function) 时位置要固定。
	* ：- 冒号，在第一行最后要加个冒号。
	* """docstring""" - 函数说明，给使用函数这介绍该它是做什么的。
	* statement - 函数内容。

用保险产品举例，每个产品都有自己的 ID，定义 instrument 函数，它只有一个「位置参数」。


```python
def instrument(id):
    print('id:', id)
    
# 给id赋值并运行
instrument('Health')
```

    id: Health
    

当然「位置参数」可以是多个，比如 id 和 ntl (代表产品id和保费)：


```python
def instrument1(id, ntl):
    print('id:', id)
    print('nlt:', ntl)

# 给nlt赋值10000并运行
instrument1('Health', '1000')
```

    id: Health
    nlt: 1000
    

如果你没有给 ntl 赋值，程序会报错


```python
instrument1('Health')
```


    -------------------------------------------------------------------------

    TypeError                               Traceback (most recent call last)

    <ipython-input-5-c370b906220b> in <module>()
    ----> 1 instrument1('Health')
    

    TypeError: instrument1() missing 1 required positional argument: 'ntl'


怎么破？来看看「默认参数」。
#### 默认参数
![image.png](attachment:image.png)
解释一下函数里面的各个部分 (黄色高亮的是新内容)：

	* def - 定义正规函数要写 def 关键词。
	* function_name - 函数名，起名最好有意义。
	* arg1 - 位置参数 ，这些参数在调用函数 (call function) 时位置要固定。
	* arg2 = v - 默认参数 = 默认值，调用函数的时候，默认参数已经有值，就不用再传值了。
	* ：- 冒号，在第一行最后要加个冒号。
	* """docstring""" - 函数说明，给使用函数这介绍该它是做什么的。
	* statement - 函数内容。

在卖对保险产品时，通常对一个保险有个保额，然后打个折送个小礼物什么的

因此我们将 rate 设为「默认参数」，并设定一个默认值 0.8。




```python
def instrument2(id, ntl, rate=0.8):
    print('id:', id)
    print('nlt_t:', float(ntl) * float(rate))
    
instrument2('Health', '1000')
```

    id: Health
    nlt_t: 800.0
    


```python
instrument2('Health', '1000', 1)
```

    id: Health
    nlt_t: 1000.0
    

使用「默认参数」最大的好处是能降低调用函数的难度，不过有个知识点需要注意。
##### 知识点
默认函数一定要放在位置参数后面，不然程序会报错。
当然「默认参数」可以是多个
但有时在调用函数时，我们会记不住参数的顺序。比如 ntl 和 rate 的位置写反了

instrument2('Health', 1, '1000')

得到的结果毫无意义，那么记不住参数顺序怎么破？在调用参数把它的「关键字」也带上，我们就可以随便调换参数的顺序。

instrument3( 'MM1001', nlt='USD', rate=1)


#### 可变参数
在 Python 函数中，还可以定义「可变参数」。顾名思义，可变参数就是传入的参数个数是可变的，可以是 0, 1, 2 到任意个。

![image.png](attachment:image.png)
解释一下函数里面的各个部分：

	* def - 定义正规函数要写 def 关键词。
	* function_name - 函数名，起名最好有意义。
	* arg1 - 位置参数 ，这些参数在调用函数 (call function) 时位置要固定。
	* arg2 = v - 默认参数 = 默认值，调用函数的时候，默认参数已经有值，就不用再传值了。
	* *args - 可变参数，可以是从零个到任意个，自动组装成元组。
	* ：- 冒号，在第一行最后要加个冒号。
	* """docstring""" - 函数说明，给使用函数这介绍该它是做什么的。
	* statement - 函数内容。



多个产品


```python
def instrument4( id, ntl=1, curR='CNY', *args ): 
    PV = 0
    for n in args: 
        PV = PV + n
        print( 'id:', id ) 
        print( 'notional:', ntl ) 
        print( 'reporting currency:', curR ) 
        print( 'present value:', PV*ntl )

```


```python
instrument4( 'MM1001', 100, 'EUR', 1, 2, 3 )
```

    id: MM1001
    notional: 100
    reporting currency: EUR
    present value: 100
    id: MM1001
    notional: 100
    reporting currency: EUR
    present value: 300
    id: MM1001
    notional: 100
    reporting currency: EUR
    present value: 600
    

除了直接传入多个参数之外，还可以将所有参数先组装成元组DCF，用以「*DCF」的形式传入函数 (DCF 是个元组，前面加个通配符 * 是拆散元组，把元组的元素传入函数中



```python
DCF = (1, 2, 3, 4, 5)
instrument4( 'MM1001', 10, 'EUR', *DCF )
```

    id: MM1001
    notional: 10
    reporting currency: EUR
    present value: 10
    id: MM1001
    notional: 10
    reporting currency: EUR
    present value: 30
    id: MM1001
    notional: 10
    reporting currency: EUR
    present value: 60
    id: MM1001
    notional: 10
    reporting currency: EUR
    present value: 100
    id: MM1001
    notional: 10
    reporting currency: EUR
    present value: 150
    

可变参数用两种方式传入

	1. 直接传入，func(1, 2, 3)
	2. 先组装列表或元组，再通过 *args 传入，func(*[1, 2, 3]) 或 func(*(1, 2, 3))



#### 关键字参数
![image.png](attachment:image.png)
解释一下函数里面的各个部分 ：

* def - 定义正规函数要写 def 关键词。
* function_name - 函数名，起名最好有意义。
* arg1 - 位置参数 ，这些参数在调用函数 (call function) 时位置要固定。
* arg2 = v - 默认参数 = 默认值，调用函数的时候，默认参数已经有值，就不用再传值了。
* *args - 可变参数，可以是从零个到任意个，自动组装成元组。
* ** kw - 关键字参数，可以是从零个到任意个，自动组装成字典。
* ：- 冒号，在第一行最后要加个冒号。
* """docstring""" - 函数说明，给使用函数这介绍该它是做什么的。
* statement - 函数内容。



「可变参数」和「关键字参数」的同异总结如下：

* 可变参数允许传入零个到任意个参数，它们在函数调用时自动组装为一个元组 (tuple)
* 关键字参数允许传入零个到任意个参数，它们在函数内部自动组装为一个字典 (dict)





```python
def instrument5(id, ntl=1, name='Heath', *args, **kw):
    pv = 0
    for n in args:
        pv = pv + n
        print('id:', id)
        print( 'present value:', pv*ntl ) 
        print( 'keyword:', kw)
```


```python
# 如果不传入任何「关键字参数」，kw 为空集。
instrument5( 'MM1001', 100, 'EUR', 1, 2, 3 )
```

    id: MM1001
    present value: 100
    keyword: {}
    id: MM1001
    present value: 300
    keyword: {}
    id: MM1001
    present value: 600
    keyword: {}
    


```python
instrument5( 'MM1001', 100, 'EUR', 1, 2, 3, test='car' )
```

    id: MM1001
    present value: 100
    keyword: {'test': 'car'}
    id: MM1001
    present value: 300
    keyword: {'test': 'car'}
    id: MM1001
    present value: 600
    keyword: {'test': 'car'}
    


```python
instrument5( 'MM1001', 100, 'EUR', 1, 2, 3, dc='act/365', test1='car', test2='people' )
```

    id: MM1001
    present value: 100
    keyword: {'dc': 'act/365', 'test1': 'car', 'test2': 'people'}
    id: MM1001
    present value: 300
    keyword: {'dc': 'act/365', 'test1': 'car', 'test2': 'people'}
    id: MM1001
    present value: 600
    keyword: {'dc': 'act/365', 'test1': 'car', 'test2': 'people'}
    


除了直接传入多个参数之外，还可以将所有参数先组装成字典 Conv，
用以「**Conv」的形式传入函数 (Conv 是个字典，前面加个通配符 ** 是拆散字典，把字典的键值对传入函数中)


```python
DCF = (1, 2, 3, 4, 5)
Conv = {'dc':'act/365', 'bdc':'following'}
instrument5( 'MM1001', 10, 'EUR', *DCF, **Conv )
```

    id: MM1001
    present value: 10
    keyword: {'dc': 'act/365', 'bdc': 'following'}
    id: MM1001
    present value: 30
    keyword: {'dc': 'act/365', 'bdc': 'following'}
    id: MM1001
    present value: 60
    keyword: {'dc': 'act/365', 'bdc': 'following'}
    id: MM1001
    present value: 100
    keyword: {'dc': 'act/365', 'bdc': 'following'}
    id: MM1001
    present value: 150
    keyword: {'dc': 'act/365', 'bdc': 'following'}
    

#### 命名关键字参数
对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
![image.png](attachment:image.png)
解释一下函数里面的各个部分 ：

* def - 定义正规函数要写 def 关键词。
* function_name - 函数名，起名最好有意义。
* arg1 - 位置参数 ，这些参数在调用函数 (call function) 时位置要固定。
* arg2 = v - 默认参数 = 默认值，调用函数的时候，默认参数已经有值，就不用再传值了。
* *, nkw - 命名关键字参数，用户想要输入的关键字参数，定义方式是在nkw 前面加个分隔符 *。
* ：- 冒号，在第一行最后要加个冒号。
* """docstring""" - 函数说明，给使用函数这介绍该它是做什么的。
* statement - 函数内容。



如果要限制关键字参数的名字，就可以用「命名关键字参数」


```python
definstrument6( id, ntl=1, curR='CNY', *, ctp, **kw ):
    print( 'id:', id ) 
    print( 'notional:', ntl ) 
    print( 'reporting currency:', curR ) 
    print( 'counterparty:', ctp ) 
    print( 'keyword:', kw)
```


      File "<ipython-input-8-ad0665459b16>", line 1
        definstrument6( id, ntl=1, curR='CNY', *, ctp, **kw ):
                                                ^
    SyntaxError: invalid syntax
    


#### 参数组合
在 Python 中定义函数，可以用位置参数、默认参数、可变参数、命名关键字参数和关键字参数，这 5 种参数中的 4 个都可以一起使用，但是注意，参数定义的顺序必须是：


* 位置参数、默认参数、可变参数和关键字参数。
* 位置参数、默认参数、命名关键字参数和关键字参数。

要注意定义可变参数和关键字参数的语法：

* *args 是可变参数，args 接收的是一个 tuple
* **kw 是关键字参数，kw 接收的是一个 dict

命名关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。定义命名关键字参数不要忘了写分隔符 *，否则定义的是位置参数。


**警告：虽然可以组合多达 5 种参数，但不要同时使用太多的组合，否则函数很难懂。**


### 匿名函数
在 Python 里有两种函数

1. 用 def 关键词的正规函数
2. 用 lambda 关键词的匿名函数

匿名函数 (anonymous function) 的说明如下：
>![image.png](attachment:image.png)
>解释一下函数里面的各个部分：

>* lambda - 定义匿名函数的关键词。
>* argument_list - 函数参数，它们可以是位置参数、默认参数、关键字参数，和正规函数里的参数类型一样。
>* ：- 冒号，在函数参数和表达式中间要加个冒号。
>* expression - 函数表达式，输入函数参数，输出一些值。



>注意 lambda 函数没有所谓的函数名 (function_header)，这也是它为什么叫匿名函数。下面是一些 lambda 函数示例：

>lambda x, y: x*y；函数输入是 x 和 y，输出是它们的积 x*y


```python
func = lambda x, y: x*y
func(2, 3)
```




    6



lambda *args: sum(args)；#输入是任意个数的参数，输出是它们的和


```python
func = lambda *args: sum(args)
func(1, 2, 3, 4, 5)
```




    15



lambda **kwargs: 1；输入是任意键值对参数，输出是 1


```python
func = lambda **kwargs: 1
func( name='Steven', age='36' )
```




    1



### 匿名函数 Vs 正规函数
看个具体的平方函数例子：


```python
lbd_sqr = lambda x: x ** 2
lbd_sqr
```




    <function __main__.<lambda>(x)>



这个 lambda 函数 lbd_sqr 做的事和下面正规函数 sqr 做的一样：



```python
def sqr(x):
    return x ** 2
sqr
```




    <function __main__.sqr(x)>




```python
print( sqr(9) )
print( lbd_sqr(9) )
```

    81
    81
    

对于 lambda 函数，有时我们会过用 (overuse) 它或误用 (misuse) 它。

#### Misuse
* 误用情况：如果用 lambda 函数只是为了赋值给一个变量，用 def 的正规函数。


```python
lbd_sqr = lambda x: x ** 2
def sqr(x): 
    returnx ** 2
print( lbd_sqr )
print( sqr )
```

    <function <lambda> at 0x00000249B4E05048>
    <function sqr at 0x00000249B4DFBD90>
    

你看，lbd_sqr 的返回值是以 <lambda> 标识的函数，而 sqr 的返回时是以 sqr 为标识的函数，明显后者一看就知道该函数是「计算平方」用的。

#### Oversuse
* 过用情况：如果一个函数很重要，它需要一个正规的名字

有些人呐，觉得 **lambda**函数很酷，会不分场合疯狂的使用。比如下面这个例子：根据【字符长度】和【首字母】来对列表排序。


```python
colors = ["Goldenrod", "purple", "Salmon", "Cyan"]
sorted(colors, key=lambda c: (len(c), c.casefold()))
```




    ['Cyan', 'purple', 'Salmon', 'Goldenrod']



在 sorted 函数有个 key 的参数，key 的值是排序的根据。比如上面用 lambda 函数设定字符长度 len(c) 和忽略大小的首个字母 c.casefold()，c 表示具体的列表。

坦白的说，这样用 lambda 函数看起来是很酷，但是增加了使用者的「思考成本」，用 def 显性定义个函数可读性会好很多。


```python
def length_and_alphaberical(str):
    """
    return sort key: length first, then caseless string.
    """
    return (len(str), str.casefold())
sorted(colors, key=length_and_alphaberical)
```




    ['Cyan', 'purple', 'Salmon', 'Goldenrod']



用正规函数还能加个函数说明 (docstring)，再起个描述性强的函数名，让人一看就知道该函数做什么。

## 高阶函数

高阶函数 (high-order function) 在函数化编程 (functional programming) 很常见，主要有两种形式：

1. 参数是函数 (map, filter, reduce)
2. 返回值是函数 (closure, partial, currying)

### Map, Filter, Reduce
Python 里面的 map, filter 和 reduce 属于第一种高阶函数，参数是函数。这时候是不是很自然的就想起了 lambda 函数？

作为内嵌在别的函数里的参数，lambda 函数就像微信小程序一样，即用即丢，非常轻便。

首先看看 map, filter 和 reduce 的语法：

* map(函数 f, 序列 x)：对序列 x 中每个元素依次执行函数 f，将 f(x) 组成一个「map 对象」返回 (可以将其转换成 list 或 set)

* filter(函数 f, 序列 x)：对序列 x 中每个元素依次执行函数 f，将 f(x) 为 True 的结果组成一个「filter 对象」返回 (可以将其转换成 list 或 set)

* reduce(函数 f, 序列 x)：对序列 x 的第一个和第二个元素执行函数 f，得到的结果和序列 x 的下一个元素执行函数 f，一直遍历完的序列 x 所有元素。


看个具体的平方示例，用 map 函数对列表每个元素平方。


```python
lst = [1, 2, 3, 4, 5]
map_iter = map(lambda x: x ** 2, lst)
print(map_iter)
print(list(map_iter))
```

    <map object at 0x00000249B4E0D710>
    [1, 4, 9, 16, 25]
    

在 map 函数中

* 第一个参数是一个计算平方的「匿名函数」
* 第二个参数是列表，即该「匿名函数」作用的对象

注意 map_iter 是 map 函数的返回对象 (它是一个迭代器)，想要将其内容显示出来，需要用 list 将其转换成「列表」形式。有点奇怪是不是？为什么 map 函数不直接返回列表呢？看完下面「惰性求值」的知识点就明白了。

* 知识点

**惰性求值** (lazy evaluation) 也称为传需求调用 (call-by-need)，目的是最小化计算机要做的工作。

在上例中，map 函数作用到列表，并不会立即进行求平方，而是当你用到其中某些元素时才去求平方。惰性是指，你不主动去遍历它，就不会计算其中元素的值。

为什么要有 「惰性求值」呢？在本例看起来毫无必要，但试想大规模数据时，一次性处理往往抵消而且不方便，而惰性求值解决了这个问题，它把计算的具体步骤延迟到了要实际用该数据的时候。

惰性序列可以看作是一个流 (flow)，需要的时候从其中取一滴水。想想 tensorflow 里构建的流图？
![image.png](attachment:image.png)

接着再看看 filter 函数，顾名思义就是筛选函数，那么我们把刚才列表中的计数筛选出来吧。


```python
filter_iter = filter(lambda n: n % 2 == 1, lst)
print( filter_iter )
print( list(filter_iter) )
```

    <filter object at 0x00000249B4E0D438>
    [1, 3, 5]
    

在 filter 函数中

* 第一个参数是一个识别奇数的「匿名函数」
* 第二个参数是列表，即该「匿名函数」作用的对象

同样，filter_iter 作为 filter 函数的返回对象，也是一个迭代器，想要将其内容显示出来，需要用 list 将其转换成「列表」形式。

最后来看看 reduce 函数，顾名思义就是累积函数，把一组数减少 (reduce) 到一个数。



```python
from functools import reduce
reduce( lambda x,y: x+y, lst )
```




    15



在 reduce 函数中

* 第一个参数是一个求和相邻两个元素的「匿名函数」
* 第二个参数是列表，即该「匿名函数」作用的对象

在 reduce 函数的第三个参数还可以赋予一个初始值，


```python
reduce(lambda x,y: x+y, lst, 100)
```




    115



这是累积从 100 和列表 lst = [1,2,3,4,5] 的第一个元素 1 开始，一直加到整个 lst 元素遍历完，因此最后求和为 115。


## **小结**
对于 map, filter 和 reduce，好消息是，Python 支持这些基本的操作；而坏消息是，Python 不建议你使用它们。下节的「解析式」可以优雅的替代 map 和 filter。

### python 推荐
除了 Python 这些内置函数，我们也可以自己定义高阶函数，如下：


```python
def apply_to_list(fun, some_list):
    return fun(some_list)
```

这个 apply_to_list 函数和上面的 map, filter 和 reduce 的格式类型，第一个参数 fun 是可以作用到列表的函数，第二个参数是一个列表。下面代码分别求出列表中所有元素的和、个数和均值。


```python
lst = [1, 2, 3, 4, 5]
print( apply_to_list( sum, lst ) )
print( apply_to_list( len, lst ) )
print( apply_to_list( lambda x:sum(x)/len(x), lst ) )
```

    15
    5
    3.0
    

### 闭包
Python 里面的闭包 (closure) 属于第二种高阶函数，返回值是函数。下面是一个闭包函数。


```python
def make_counter(init): 
    counter = [init]
    def inc(): 
        counter[0] += 1
    def dec(): 
        counter[0] -= 1
    def get():
        return counter[0]
    def reset(): 
        counter[0] = init
    return inc, dec, get, reset
```

此函数的作用是做一个计数器，可以

* 用增加子函数 inc() 续一秒
* 用减少子函数 dec() 废一秒
* 用获取子函数 get() 看秒数 
* 用重置子函数 reset() 回原点




```python
inc, dec, get, reset = make_counter(0)
inc()
inc()
inc()
get()
```




    3



续了三秒。


```python
dec()
get()
```




    2



减了一秒，相当于续了两秒。


```python
reset()
get()
```




    0



重新计秒

属于第二类 (返回值是函数) 的高阶函数还有「偏函数」和「柯里化」，由于它们比较特别，因此专门分两节来讲解。


### 偏函数
偏函数 (paritial function) 主要是把一个函数的参数 (一个或多个) 固定下来，用于专门的应用上 (specialized application)。要用偏函数用从 functools 中导入 partial 包：


```python
from functools import partial
```

举个排序列表里元素的例子


```python
lst = [1, 2, 3, 4, 5]
sorted(lst)
```




    [1, 2, 3, 4, 5]



我们知道 sort 函数默认是按升序排列，假设在你的应用中是按降序排列，你可以把函数里的 reverse 参数设置为 True。


```python
sorted(lst, reverse=True)
```




    [5, 4, 3, 2, 1]



这样每次设定参数很麻烦，你可以专门为「降序排列」的应用定义一个函数，比如叫 sorted_dec，用偏函数 partial 把内置的 sort 函数里的 reverse 固定住，代码如下：


```python
sorted_dec = partial( sorted, reverse=True )
sorted_dec
```




    functools.partial(<built-in function sorted>, reverse=True)



不难发现 sorted_dec 是一个函数，而且参数设置符合我们的应用，把该函数用到列表就能对于降序排列。


```python
sorted_dec( lst )
```




    [5, 4, 3, 2, 1]



小结，当函数的参数个数太多，需要简化时，使用 functools.partial 可以创建一个新的函数，即偏函数，它可以固定住原函数的部分参数，从而在调用时更简单。

### 柯里化
最简单的柯里化 (currying) 指的是将原来接收 2 个参数的函数 f(x, y) 变成新的接收 1 个参数的函数 g(x) 的过程，其中新函数 g = f(y)。

以普通的加法函数为例：


```python
def add1(x, y):
    return x + y
```

通过嵌套函数可以把函数add1转换成柯里化函数add2


```python
def add2(x):
    def add(y):
        return x + y
    return add
```

仔细看看函数 add1 和 add2 的参数 (常数用红色表示)

* add1：参数是 x 和 y，输出 x + y
* add2：参数是 x，输出 x + y
* g = add2(2)：参数是 y，输出 2 + y

下面代码也证实了上述分析：



```python
add1
add2
g = add2(2)
g
```




    <function __main__.add2.<locals>.add(y)>




```python
print(add1(2, 3))
print(add2(2)(3))
print(g(3))
```

    5
    5
    5
    

## 解析式
解析式 (comprehension) 是将一个可迭代对象转换成另一个可迭代对象的工具。

上面出现了两个可迭代对象 (iterable)，不严谨地说，容器类型数据 (str, tuple, list, dict, set) 都是可迭代对象。

* 第一个可迭代对象：可以是任何容器类型数据。
* 第二个可迭代对象：看是什么类型解析式：


* 列表解析式：可迭代对象是 list
* 字典解析式：可迭代对象是 dict
* 集合解析式：可迭代对象是 set


下面写出列表、字典和集合解析式的伪代码 (pseudo code)。


```python
# list comprehension
[值 for 元素 in 可迭代对象 if 条件]

# dict comprehension
{键值对 for 元素 in 可迭代对象 if 条件}

# set comprehension
{值 for 元素 in 可迭代对象 if 条件} 
```


    -------------------------------------------------------------------------

    NameError                               Traceback (most recent call last)

    <ipython-input-73-5cccff3d88fb> in <module>()
          1 # list comprehension
    ----> 2 [值 for 元素 in 可迭代对象 if 条件]
          3 
          4 # dict comprehension
          5 {键值对 for 元素 in 可迭代对象 if 条件}
    

    NameError: name '可迭代对象' is not defined


不难发现，这些解析式都有

* for ... in ...：这不就是个「for 循环」么？
* if：这不就是个「if 条件」么？

对，解析式就是为了把「带条件的 for 循环」简化成一行代码的。

也不难发现，列表解析式整个语句用「中括号 []」框住，而字典和集合解析式整个语句中「大括号 {}」框住。想想 list, dict 和 set 用什么括号定义就明白了。

通过这两个发现，我们大概对解析式有个一些直观但还比较模糊的理解，根据 input-operation-output 这个过程总结：

* input：任何「可迭代数据 A」
* operation：用 for 循环来遍历 A 中的每个元素，用 if 来筛选满足条件的元素 Agood
* output：将 Agood 打包成「可迭代数据」，生成列表用 []，生成列表用 {}

有点抽象？我知道，下节用「列表解析式」来进一步举例说明。

#### 列表解析式
问题： 如何从一个含证书列表中把奇数（odd number）条数出来


```python
lst = [1, 2, 3, 4, 5]
odds = []
for i in lst:
    if i % 2 == 1:
        odds.append(i)
odds
    
```




    [1, 3, 5]



任务完成了，但这个代码有好几行呢，不简洁，看看下面这一行代码：



```python
odds = [i for i in lst if i % 2 == 1]
odds
```




    [1, 3, 5]



从「for 循环」到「解析式」不直观，我来用不同颜色把这个过程可视化一下，如下图：
![image.png](attachment:image.png)
可以把「for 循环」到「解析式」的过程想像成一个「复制-粘贴」的过程：

1. 将「for 循环」的新列表复制到「解析式」里
2. 将 append 里面的表达式n * 2复制到新列表里
3. 复制循环语句 for n in lst 到新列表里，不要最后的冒号
4. 复制条件语句 if n%2 == 1 到新列表里，不要最后的冒号

现在清楚多了吧，在把上面具体的例子推广到一般的例子，从「for 循环」到「列表解析式」的过程如下：

![image.png](attachment:image.png)


因此现在你可以一口气写出「列表解析式」了吧，或者可以一口气读懂别人写的「列表解析式」了吧。下节我们会用几个实例来巩固下理解。

现在你可能会说上面「for 循环」只有一层，如果两层怎么转换「列表解析式」？具体来说怎么解决下面这个问题。




问题：如何用「列表解析式」将一个二维列表中的元素按行一个个展平？

没思路？先用「for 循环」试试？


```python
flattened = []
for row in lst:
    for n in row: 
        flattened.append(n)
```


    -------------------------------------------------------------------------

    TypeError                               Traceback (most recent call last)

    <ipython-input-78-0e14db71c985> in <module>()
          1 flattened = []
          2 for row in lst:
    ----> 3     for n in row:
          4         flattened.append(n)
    

    TypeError: 'int' object is not iterable


套用一维「列表解析式」的做法
![image.png](attachment:image.png)

两点需要注意：

1. 该例没有「if 条件」条件，或者认为有，写成「if True」。如果有「if 条件」那么直接加在「内 for 循环」后面。
2. 「外 for 循环」写在「内 for 循环」前面。


我承认我一开始也习惯写成下图错误的那种 (多练几次就可以改过来了)，
![image.png](attachment:image.png)



#### 其它解析式
我们把「列表解析式」那一套举一反三的用到其他解析式上，用下面两图理解一下「字典解析式」和「集合解析式」。
![image.png](attachment:image.png)

![image.png](attachment:image.png)

### 小结
再回顾下三种解析式，我们发现其实它们都可以实现上节提到的 filter 和 map 函数的功能，用专业计算机的语言说，解析式可以看成是 filter 和 map 函数的语法糖。

#### 知识点
语法糖 (syntactic sugar)：指计算机语言中添加的某种语法，对语言的功能没有影响，但是让程序员更方便地使用。

语法盐 (syntactic salt)：指计算机语言中添加的某种语法，使得程序员更难写出坏的代码。

语法糖浆 (syntactic syrup)：指计算机语言中添加的某种语法，没能让编程更加方便。

了解完概念，我们看看为什么说「列表解析式」是 「map/filter」的语法糖，两者的类比图如下：

![image.png](attachment:image.png)

首先发现两者都是把原列表根据某些条件转换成新列表，再者

「列表解析式」用if 条件来做筛选得到 item，再用 f 函数作用到 item 上。

「map/filter」用 filter 函数来做筛选，再用 map 函数作用在筛选出来的元素。

为了达到相同目的，明显「列表解析式」是种更简洁的方式。

用「在列表中先找出奇数再乘以 2」的例子，对于列表 lst = [1, 2, 3, 4, 5]，我们先看「列表解析式」的实现：


```python
[ n*2 for n in lst if n%2 == 1]
```




    [2, 6, 10]



再看「map/filter」的实现：


```python
list( map(lambda n: n*2, filter(lambda n: n%2 == 1, lst)) )
```




    [2, 6, 10]



#### 小例子
问题：用解析式将二维元组里每个元素提取出来并存储到一个列表中。



```python
tup = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
```

先遍历第一层元组，用 for t in tup，然后遍历第二层元组，用 for x in t，提取每个 x 并"放在“列表中，用 []。代码如下：



```python
flattened = [x for t in tup for x in t]
flattened

```




    [1, 2, 3, 4, 5, 6, 7, 8, 9]




至于为什么按 for t in tup for x in t 这个顺序写，还记得上节的这张图吗？
![image.png](attachment:image.png)

如果我们想把上面「二维元组」转换成「二维列表」呢？


```python
[ [x for x in t] for t in tup ]
```




    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



### others eg:
回到上篇引言的问题。



问题：用解析式把以下这个不规则的列表 a 打平 (flatten)?

a = [1, 2, [3, 4], [[5, 6], [7, 8]]]

用解析式一步到位解决上面问题有点难，特别是列表 a 不规则，每个元素还可以是 n 层列表，因此我们需要递推函数 (recursive function)，即一个函数里面又调用自己。


```python
a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
def f(x):
    if type(x) is list:
        return [y for l in x for y in f(l)]
    else :
        return [x]
f(a)
```




    [1, 2, 3, 4, 5, 6, 7, 8]



整个列表遍历一遍，有四个元素，1,2, [3, 4] 和 [[5, 6], [7, 8]]。函数 f(x) 是一个递推函数，当 x 是元素，返回 [x]，那么

* f(1) 的返回值是 [1]
* f(2) 的返回值是 [2]

当 x 是列表，返回 [y for l in xfor y in f(l)]，当 x = [3 ,4] 时

* for l in x：指的是 x 里每个元素 l，那么 l 遍历 3 和 4
* for y in f(l)：指的是 f(l) 里每个元素 y

   * 当 l = 3，是个元素，那么 f(l) = [3], y 遍历 3
	* 当 l = 4，是个元素，那么 f(l) = [4], y 遍历 4

整个 f([3 ,4]) 的返回值是 [3 ,4]。同理，当 x = [[5, 6], [7, 8]] 时，f(x) 的返回值是 [5, 6, 7, 8]。

到此，列表中四个元素 1, 2, [3, 4] 和 [[5, 6], [7, 8]] 的情况都分析完毕了，现在当 x = [1, 2, [3, 4], [[5, 6], [7, 8]]]，f(x) 也运行到下面这步

`return [y for l in x for y in f(l)]`

那么

* 当 x = 1, 有 f(1) = [1],  y = 1
* 当 x = 2, 有 f(2) = [2],  y = 2
* 当 x = [3, 4], 有 f([3, 4]) = [3, 4],  y = 3, 4
* 当 x = [5, 6, 7, 8], 有 f([5, 6, 7, 8]) = [5, 6, 7, 8],  y = 5, 6, 7, 8

把这所有的 y 再合成一个列表不就是

`
[1, 2, 3, 4, 5, 6, 7, 8]

`
正规 (递推) 函数写好了，把它写成匿名函数也很简单了。


```python
a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
f = lambda x: [y for l in x for y in f(l)] if type(x) is list else [x]
f(a)
```




    [1, 2, 3, 4, 5, 6, 7, 8]



理解：
![image.png](attachment:image.png)

# 6总结
本帖讨论了函数和解析式。优雅清晰是 python 的核心价值观，高阶函数和解析式都符合这个价值观。

函数包括正规函数 (用 def) 和匿名函数 (用 lambda)，函数的参数形态也多种多样，有位置参数、默认参数、可变参数、关键字参数、命名关键字参数。匿名函数主要用在高阶函数中，高阶函数的参数可以是函数 (Python 里面内置 map/filter/reduce 函数)，返回值也可以是参数 (闭包、偏函数、柯里化函数)。

解析式并没有解决新的问题，只是以一种更加简洁，可读性更高的方式解决老的问题。解析式可以把「带 if 条件的 for 循环」用一行程序表达出来，也可以实现 map 加 filter 的功能。

最后用 Tim Peters 的 The Zen of Python 结尾。


`Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one -- and preferably only one -- obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
`
### 翻译和解释
`
Python之禅 by Tim Peters

优美胜于丑陋（Python 以编写优美的代码为目标）

明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）

简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）

复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）

扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）

间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）

可读性很重要（优美的代码是可读的）

即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上）
 
不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写 except:pass 风格的代码）
 
当存在多种可能，不要尝试去猜测

而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）

虽然这并不容易，因为你不是 Python 之父（这里的 Dutch 是指 Guido ）
 
做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量）
 
如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准）
 
命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）
`

