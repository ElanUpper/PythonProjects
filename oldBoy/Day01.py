# author: elan

import sys
print(sys.path)
print(sys.path.__doc__)
print(sys.argv)

# os operation system
# os.system 仅仅返回执行结果 0表示成功
# os.popen  返回进程文件指针 需要用read读取
import os
dir_list = os.system("dir")
print(type(dir_list), 'dir list:', dir_list)

dir_list_1 = os.popen("dir") # 结果返回一个进程文件指针
print(type(dir_list_1), 'dir list:', dir_list_1.read())

# mkdir
#os.mkdir("elan")

from elan import printname as pn
pn.printUser('elan')

b_hello = 'hello_你好'.encode('utf-8')
hello=b_hello.decode('utf-8')
print(b_hello, hello)


arr_num = [1,2,3,4,5,6,7,2]

# 插入元素
arr_num.append(3)
print(arr_num)
arr_num.insert(3, -1) # 插入到的位置从0开始  value
print(arr_num)


# 查找元素所有对应索引
start_index = 0
search_num = 2
search_arr = [];
for i in range(arr_num.count(search_num)):
    start_index = arr_num.index(search_num, start_index) ;
    search_arr.append(start_index) ;
    # 修改数据 所有2为-3
    arr_num[start_index] = -1 * search_num
    start_index += 1 ;
print('change list:', arr_num, search_arr)


# 删除指定所有元素
del_num = 2
for i in range(arr_num.count(del_num)):
    arr_num.remove(del_num)
print('after delete list:', arr_num)


# 拷贝元素
## 浅拷贝
arr_copy  = arr_num
arr_copy1 = arr_num.copy()
print(id(arr_num), id(arr_copy), id(arr_copy1))
arr_nest = [1, 2, arr_num]
arr_nest_copy  = arr_nest
arr_nest_copy1 = arr_nest.copy()
# check the nested data, found the data pointer is same
print(id(arr_nest[2]), id(arr_nest_copy[2]), id(arr_nest_copy1[2]))

## 深拷贝
import copy
arr_nest = [1, 2, arr_num]
arr_nest_copy  = copy.copy(arr_nest)
arr_nest_copy0 = list(arr_nest)
arr_nest_copy1 = arr_nest[:]
arr_nest_copy2 = copy.deepcopy(arr_nest)
# check the nested data, found the data pointer is same
print(id(arr_nest[2]), id(arr_nest_copy[2]), id(arr_nest_copy0[2]),
      id(arr_nest_copy1[2]), id(arr_nest_copy2[2]))


# 购物车
Good_list = ['Car:20000', 'Bike:1000', 'Soup:10', 'Cat:200'];
Good_tmp = [('car', 200), ('bike', 100)]
Cart_list = [];

Good_str = '''
  title  Fee
   {}    {}
   {}    {}
   {}    {}
   {}    {}
  tips: q for exit this program!!
'''.format(Good_list[0].split(':')[0], Good_list[0].split(':')[1],
           Good_list[1].split(':')[0], Good_list[1].split(':')[1],
           Good_list[2].split(':')[0], Good_list[2].split(':')[1],
           Good_list[3].split(':')[0], Good_list[3].split(':')[1] );

while True:
  Salary_input = input('input your salary: ')
  if Salary_input.isdigit():
      break;
  else:
      print('input valid salary. ')

Salary_init = int(Salary_input) ;

while Salary_init >= 0 :
  goods_money = 0 ;
  print(Good_str);
  print('your current money: {}'.format(Salary_init))
  choice = input('input which one you want to buy: ');
  if (choice.upper() == Good_list[0].split(':')[0].upper() ) :
      goods_money = int(Good_list[0].split(':')[1]);
  elif (choice.upper() == Good_list[1].split(':')[0].upper() ) :
      goods_money = int(Good_list[1].split(':')[1]) ;
  elif (choice.upper() == Good_list[2].split(':')[0].upper() ) :
      goods_money = int(Good_list[2].split(':')[1]);
  elif (choice.upper() == Good_list[3].split(':')[0].upper() ) :
      goods_money = int(Good_list[3].split(':')[1]) ;
  elif (choice.upper() == 'Q'):
      break ;
  else :
      print('wrong choice %s !!!'%choice)  # 第一种格式化字符串标准
      continue ;

  # 如果金额大于0 才可以计算为商品购买成功
  if Salary_init >= goods_money  :
    Cart_list.append(choice)
    Salary_init -= goods_money ;
  else :
    print('you have no money to afford it!')

print(Cart_list) ;


