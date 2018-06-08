# author: elan

# 经典类
print('经典类'.center(100, '-'));

class base:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class fath_1(base):

    def get_name(self):
        return 'fath_1';

class fath_2(base):

    def get_name(self):
        return 'fath_2';

class fath_3(fath_1, fath_2):

    def get_name(self):
        return 'fath_3';

tester = fath_3('elan');
print(tester.get_name())

# 新类
print('新类'.center(100, '-'));

class base_new(object):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class fath_1_new(base_new):

    pass

class fath_2_new(base_new):

    def get_name(self):
        return 'fath_2';

class fath_3_new(fath_1_new, fath_2_new):

    pass

tester_new = fath_3_new('elan');
print(tester_new.get_name())

# python2&3 均采用宽度优先
# python2 经典类采用深度优先   新类采用宽度优先

# 鸭子类型
def fun_pass_cls(base):
    print(base.get_name())

f1 = fath_1('elan');
f2 = fath_2('jade');

fun_pass_cls(f1)
fun_pass_cls(f2)

#
class senior_guy:
    """ demo: senior guy """
    level = 'senior'
    count = 0

    def __init__(self, name):
        self.name = name
        senior_guy.count += 1;

    # p_name property
    @property
    def p_name(self):
        return self.name

    @p_name.setter
    def p_name(self, name):
        self.name = name

    @p_name.deleter
    def p_name(self):
        del self.name

    # 静态字段 NAME
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def del_name(self):
        del self.name

    # 依次是 get方法 set方法 删除方法  文档说明
    NAME = property(get_name, set_name, del_name, 'NAME的构造方法')

    @classmethod
    def cls_level(cls):
        return senior_guy.level

    @staticmethod
    def cls_count():
        return senior_guy.count ;


# 打印文档说明
print(senior_guy.__doc__)
# 静态属性 静态方法
print(senior_guy.level, senior_guy.cls_level());
elan = senior_guy('elan');
# class方法->属性   静态方法
print(elan.p_name, elan.cls_count())
jade = senior_guy('jade');
print(jade.cls_count())

#定义属性共有两种方式，分别是【装饰器】和【静态字段】
# 1. class的property方法 getter setter deleter
elan.p_name = 'upd';
print(elan.p_name)
del elan.p_name
print(elan.p_name)
# 2. class的静态property NAME
elan.Name = 'Named';
print(elan.Name)
del elan.Name
print(elan.Name)




