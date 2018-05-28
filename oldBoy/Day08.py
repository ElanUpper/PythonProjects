# author: elan

# 匿名函数+列推导式
func = lambda x:x*2
listA = [ func(x) for x in range(10) if x%2 == 0 ]
print(listA)


###  --------------
def fib(max):
    RetList = [1, 1]
    n, a, b = 2, 1, 1
    while n < max:
        a, b = b, b+a
        # 相当于下面语句
        #   1. t = (b, b+a)
        #   2. a = t[0]  b = t[1]
        RetList.append(b)
        n += 1
    return RetList

print(fib(9))

###  -------------- 生成器升级版
def fib_iterator(max):
    n, a, b = 2, 1, 1
    yield(a)
    yield(b)
    while n < max:
        a, b = b, b+a
        yield(b)
        n += 1

for item in fib_iterator(9) :
    #print(item)
    pass

# -- 生成器实现 并发
def customer(name):
    print('{0}要开始吃荔枝了！'.format(name));
    while True:
        i = yield  # 通过yield 获取send过来的数据
        #print('%s要开始吃%s个荔枝了！'%(name, i));


c1 = customer('elan');
c2 = customer('jade');
c1.__next__();
c2.__next__();
for i in range(10):
    c1.send(i);
    c2.send(i);

# 可以用for循环的叫 可迭代对象 iterable
# 可以用next函数并不断返回下一个值的对象 叫迭代器 iterator
# 判断是否是可迭代对象 迭代器
from collections import Iterable, Iterator
# str
print(isinstance('', Iterable), isinstance('', Iterator))
# list
print(isinstance([], Iterable), isinstance([], Iterator))
# set
print(isinstance({}, Iterable), isinstance({}, Iterator))
# tuple
print(isinstance((), Iterable), isinstance((), Iterator))
# generator
print(isinstance((x for x in range(10)), Iterable), isinstance((x for x in range(10)), Iterator))
# int
print(isinstance(10, Iterable), isinstance('', Iterator))
# list dict str 可以通过iter
lista = iter([])
print(isinstance(lista, Iterable), isinstance(lista, Iterator))

# 进一步剖析range
for i in range(2):
    print(i)
## 跟上面等价
riter = iter([0, 1]);
while True:
    try:
        x = riter.__next__(); # next(riter)
        print(x)
    except StopIteration:
        break
# 进一步证明
print(range(2), type(range(2)) )
print(isinstance(range(2), Iterator))


