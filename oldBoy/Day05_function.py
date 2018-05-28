# author: elan

def default_args(x=10, y=20):
    print(x, y)

# 一个星（*）：表示接收的参数作为元组来处理 仅仅可以处理位置参数
def array_args(*argv):
    for num, val in enumerate(argv):
        print("Item %s %s"% (num, val))

# 两个星（**）：表示接收的参数作为字典来处理 仅仅可以处理keywords参数
def dicts_args(**argv):
    for key, val in argv.items():
        print("Item %s %s"% (key, val))
    print(argv.get('name'), argv.get('age'), argv.get('salary'))

def array_dict_args(name, *arga, **argd):  # 位置不可以调换变为 **argd, *arga
    print('name = %s'% name);
    print(arga);
    print('**argd = %s'% argd);

if __name__ == '__main__' :

  # 调用默认参数
  default_args()

  # 处理不定参数组
  array_args(1,2,3,4)
  print(''.center(30, '-'))
  array_args(*[1,2,3,4])
  print(''.center(30, '-'))

  # 传入字典
  dicts_args(name='elan', age='30', salary='20000')
  print(''.center(30, '-'))
  dicts_args(**{'name': 'elan', 'age': '30', 'salary': '20000'})
  print(''.center(30, '-'))

  # *argv  **argv混合使用
  # array_dict_args(name='elan', '20', 'man')  # error positional argument follows keyword argument
  array_dict_args(name='elan', arga=('20', 'man'), argd={'age':'20', 'gender':'man'})
