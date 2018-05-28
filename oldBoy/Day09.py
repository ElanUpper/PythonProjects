# author: elan

# 内置方法 build-in functions

# 1. abs 取绝对值
# print(abs(-1))

# 2. all 如果可迭代对象集合都为真 那么返回真 否则为假
#print(all( [-1, 1, 0] ))

# 3. any 如果可迭代对象集合一个为真 那么返回真 否则为假
#print(any( [-1, 1, 0] ))

# 4. ascii 将对象转换为string
# print(type(ascii(['hello', '你好'])))  # <class 'str'>

# 5. bin  将数字转换为二进制
# print(bin(10))   # 0b1010

# 6 判断值是否为真
# print(bool([]))

# 7. bytes 转换
# retBytes = bytes("abcd", encoding='utf-8');
# print(retBytes.capitalize(), retBytes)
# ArrBytes = bytearray("abcd", encoding='utf-8');
# print(ArrBytes, ArrBytes[1])
# ArrBytes[1] = 66
# print(ArrBytes, ArrBytes[1])

# 8. callable 判断是否可以调用  简单判断 对象可以加()就可以被调用
# class ClassP():
#     def __init__(self):
#       pass
# def fun_demo(): pass ;
# print(callable(ClassP), callable(fun_demo)); # True

# 9. 将数字转换为asci码  asc码转换为数字
# print(chr(97))
# print(ord('a'))

# 10. compile
# code_class = '''
# class student():
#   def __init__(self):
#     self.name = '';
#   def set_name(self, name):
#     self.name = name;
#   def get_name(self):
#     return self.name;
#
# if __name__ == '__main__':
#   stu = student();
#   stu.set_name('elan');
#   print('the name is ', stu.get_name());
# '''
# pyObj1 = compile(code_class, 'log.txt', 'exec');
# exec(pyObj1);
#
# code_math = '1+2/2 *6';
# pyObj0 = compile(code_math, '', 'eval');
# print(eval(pyObj0))
# print(eval(code_math));

# 11. 查看xx具有的方法
# print(dir( dict() ))

# 12. divmod 返回商和余数
# print(divmod(5, 2))

# 13. enumerate 如果不用start index默认是从0开始
# lista = ['a', 'b', 'c']
# print(list(enumerate(lista, start=1)))


# 14.lamdab   lambda[arg1 [, agr2,.....argn]] : expression

# lambda于def区别
# 1）lambda会返回一个函数对象，但这个对象不会赋给一个标识符，而def则会把函数对象赋值给一个变量（函数名）。 两个是<class 'function'>
# 2）lambda只是一个表达式，而def则是一个语句。 主要用于简化代码
# 3）lambda表达式:后面，只能有一个表达式(if或for或print等语句不能用)，def则可以有多个并且可以定义复杂的函数
# 4）lambda函数不能共享给别的程序调用，def可以。
# funct1 = lambda x: x+1 ;
# def funct2(x):
#     return x+1;
# print(type(funct1), funct1, type(funct2), funct2)

# 结合三元运算符 <True expression> if <condition> else <False expression>
#   print((lambda x: 10 if x > 10 else x)(9))
# 结合filter Return an iterator which function(item) is true.
#   def __init__(self, function_or_None, iterable
#   for item in filter(lambda x:1 if x > 5 else 0, range(10)):
#   for item in filter(lambda x:x > 5, range(10)):
#     print(item)
# 结合map  对每一个item进行function计算
#for item in map(lambda x:x*x, range(10)):
#    print(item)
#类似于下面代码
# for item in [x*x for x in range(10) if x > 0]:
#     print(item)
# # list comprehension for lambda
# for item in [(lambda x: x*x if x > 0 else '-')(x) for x in range(10)]:
#     print(item)
# # list comprehension if nested if  > 5 good   3~5 well <3 bad
# for item in [(lambda x: 'good' if x > 5 else ('well' if x > 3 else 'bad') )(x) for x in range(10)]:
#     print(item)
# 结合reduce  将两个item进行function计算 最终返回一个总结果
# import functools
# print(functools.reduce(lambda x, y:x+y, range(10)))
# 结合sorted  Return a new list containing all items from the iterable in ascending order.
# 要求按照绝对值大小排序
#list_raw = [3, -1, 4, -3, 0, -5];
#print(sorted(list_raw, key=lambda x:abs(x)))
# dict_raw = {1:2, -1:-3, -3:2, 0:10, 20:3, 4:2};
## 按照dict-key排序
# print(sorted(dict_raw.items()))
## 按照dict-value排序
# print(sorted(dict_raw.items(), key=lambda x:x[1]))

# 15. frozenset变为不可变set  该集合跟tuple list一样
# set1 = frozenset([1, 2, 3, 4])

# 16. globals  以key:value形式返回整个程序中静态所有变量
# print(globals())

# 17. hex 10进制->16进制
#print(hex(244))  # 0xf4

# 18. len 返回长度
# print(len('abcd')) # 4
# print(len({'name':'elan', 'nakename':'elan2'})) # 2 字典个数


# 19. locals 打印局部变量 仅仅在自己的作用域中 globals是全局哪里都一样
# def fun_local1():
#     lc_var = 10;
#     print(locals());
# def fun_local2():
#     lc_var = 20;
#     print(locals());
# fun_local1();
# fun_local2();
# print(locals())

#20. max min

#21. next
# Return the next item from the iterator. call the method __next__
# If default is given and the iterator is exhausted, it is returned instead of raising StopIteration.

# 22 oct
#print(oct(200))  # 0oxxx

# 23 pow   Equivalent to x**y (with two arguments) or x**y % z (with three arguments)
#print(pow(2, 5), pow(2, 3, 3))

#24. range
# range(stop) -> range object
# range(start, stop[, step]) -> range object

#25. reversed  Return a reverse iterator
# list_s = [1, 2, 3, 4]
# # 下面展示两种由iterator到list的方法
# print(list(reversed(list_s)), [item for item in reversed(list_s)],  list_s);

#26. round    Round a number to a given precision in decimal digits (default 0 digits)
#print(round(10.22, 3))

#27. sum  Return the sum of a 'start' value (default: 0) plus an iterable of numbers
# lista = [x for x in range(10)]
# print(sum(lista), sum([]))

#28. zip
# zip(iter1 [,iter2 [...]]) --> zip object iterator
# lista = [1, 2, 3, (1, 2)]; listb=['a', 'b', 'c', 'd', 'e']
# print(list(zip(lista, listb)))

#29. __import__  Import a module 使用字符串
#__import__('Day01')