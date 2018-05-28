# author: elan
# set programming

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 6, 7}

# 添加 字符串与数字
set1.add('6')
set1.add(6)
print('set1: ', set1)

# 删除
set1.remove('6')
print('set1: ', set1)

print('Set1: ', set1, ' Set2: ', set2 )
print("---------------------------------------------")
# 交集
print(set1.intersection(set2))
print(set1 & set2)
print("---------------------------------------------")
# 并集
print(set1.union(set2))
print(set1 | set2)
print("---------------------------------------------")
# 差集  在set1中不在set2中
print(set1.difference(set2))
print(set1 - set2 )
print("---------------------------------------------")
# 反集  删除set1 & set2共有的元素
print(set1.symmetric_difference(set2))
print(set1 ^ set2)
print("---------------------------------------------")
# 判断子集
setc = {3, 4}
print('{} is subset {}? '.format(setc, set1), setc.issubset(set1))
print('{} is subset {}? '.format(setc, set2), setc.issubset(set2))

# 判断父集
setf = {3, 4, 6, 7, 0}
print('{} is superset {}? '.format(setf, set1), setf.issuperset(set1))
print('{} is superset {}? '.format(setf, set2), setf.issuperset(set2))

# 判断是否有交集
SetA = {'a', 'b', 'c', '4'}
SetB = {'1', '2', '3', 'd'}
print('Is %s contain no one in %s?'%(SetA, SetB), SetA.isdisjoint(SetB))

# 添加元素
SetA.add('!')
SetA.update(['e', 'f', 'g'])
print(SetA)

# 删除
SetA.remove('!')
SetA.discard('!')  # 如果删除的不在set中 那么不会报错  remove会报错
# 判断是否是Set中一个成员
print('a' is SetA)