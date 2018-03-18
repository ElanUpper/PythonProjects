# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Demo
   Description :
   Author :       elan
   date：          3/9/2018
-------------------------------------------------
   Change Activity:
                   3/9/2018:
-------------------------------------------------
"""

from random import randint

# 1、字典（dict）
print('----------------------- dict --------------------------')
dict = {'name': 'Zara', 'age': 7, 'class': 'First'}

## 1.1 字典——字符串
print (type(str(dict)), str(dict))

## 1.2 字典——元组 key
print (tuple(dict))  # 返回：('age', 'name', 'class')
print (tuple(dict.keys()))  # 返回：('age', 'name', 'class')

## 1.3 字典——元组 value
print (tuple(dict.values())) # 返回：(7, 'Zara', 'First')

## 1.4 字典——列表
print (list(dict)) # 返回：['age', 'name', 'class']
print ( (k, v) for k in dict.keys() for v in dict.values() )

## 1.5 字典——列表
print (dict.values)


# 2、元组
print('----------------------- tuple --------------------------')
tup=(1, 2, 'c', 4, 'a')

## 2.1 元组——字符串
print (tup.__str__())  # 返回：(1, 2, 3, 4, 5)

## 2.2 元组——列表
print (list(tup))  # 返回：[1, 2, 3, 4, 5]

## 2.3 元组--字典 不可能(缺少keys)
print ({ k:v for k in range(len(tup)) for v in tup }) # 返回 {0: 'a', 1: 'a', 2: 'a', 3: 'a', 4: 'a'}
print ({ k:v for k in range(len(tup)) for v in tup if v == tup[k] })

# 3、列表
print('----------------------- list --------------------------')
nums=[1, 3, 5, 7, 8, 13, 20];

## 3.1 列表——字符串
print (str(nums))  # 返回：[1, 3, 5, 7, 8, 13, 20]

## 3.2 列表——元组
print (tuple(nums)) # 返回：(1, 3, 5, 7, 8, 13, 20)

## 3.3 列表--字典  不可能(缺少keys)


# 4、字符串
print('----------------------- string --------------------------')
## 4.1 字符串——元组
print (tuple(eval("(1,2,3)")))  # 返回：(1, 2, 3)

## 4.2 字符串——列表
print (list(eval("(1,2,3)")))  # 返回：[1, 2, 3]

## 4.3 字符串——字典  不可能(缺少keys)

# print (type(eval("{'name':'ljq', 'age':24}"))) # 返回：
# print([ x*x for x in range(10) if x%2 == 0 ])

print("-------------------- 特殊测试 -----------------------------")

# 生成10个-10,10的数字
data1 = [randint(-10, 10) for _ in range(10)]
# function filter
def def_filter(data):
  return filter(lambda x: x>0, data)
# list comprehension
def def_list_comprehension(data):
	return [x for x in data if x > 0]
print( list(def_filter(data1)) )
print( list(def_filter(data1)) )

# 字典过滤
data_dict = { x:randint(-100, 10) for x in range(10) }
data_dict1 = { k:v for k,v in data_dict.items() if v > 0 }
print(data_dict)
print(data_dict1)

# 集合过滤
data_set = { randint(-100, 10) for x in range(10) if x % 2 == 0 }
data_set1 = list(def_filter(data_set))
print(data_set)
print(data_set1)