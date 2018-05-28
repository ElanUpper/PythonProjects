# author: elan

import time

def calc_two_number(a, b):
    time.sleep(1);
    return [a, b, int(a+b)];

def get_func_run_time(func, *argv):
    start_time = time.time();
    print(func(*argv));
    end_time = time.time();
    print('the function run time %s'%(end_time - start_time));

get_func_run_time(calc_two_number, 10, 20)

# 通过装饰器获取函数执行时间
# 装饰器 就是让使用者感觉它是透明的
#   1. 首先不改变使用者的调用方式以及参数
#   2. 其次不修改使用者的任何功能(源代码)，仅仅提供一个附件功能
import time
def timer(func):
    def wrapper(*args, **argv):
        start_time = time.time();
        func(*args);
        end_time = time.time();
        print('the function run time %s'%(end_time - start_time))
    return wrapper;

#---------------------------------------------
# 纯粹测试@fun 高阶是否纯粹的替换地址
def fun_ret_fun(func_memory_id):  # 装饰器function地址 参数:被调用函数地址
    def inner_func():
        print('被调用函数地址: ', id(func_memory_id));
    return inner_func;

@fun_ret_fun
def fun_test_suger():  # 被装饰funcion
    print('called');

@fun_ret_fun
def fun_test_suger2():  # 被装饰funcion
    print('called');


print('@语法糖测试:\n被装饰funcion地址:', id(fun_test_suger),
      ' \n装饰器function地址:', id(fun_ret_fun),
      '\n',fun_test_suger());

print('@语法糖测试:\n被装饰funcion地址:', id(fun_test_suger2),
      ' \n装饰器function地址:', id(fun_ret_fun),
      '\n',fun_test_suger2());


# 测试结论： 果然是地址替换  但是@替换function地址 必须带一个参数：为了接受被替换函数的地址，方便在后面运行这个函数
# 还有一个更为重要的特点: 如果我们用id查看被装饰器装饰的函数，那么它的内存id 会比 之前还没有被修饰的内存id不同！！！！
#                     我们在清晰的解释下这个现象 @替换了函数的入口地址


# 高阶函数
# 把一个函数名当做实参传给另外一个函数（在不修改被装饰的函数代码的情况下为它添加功能）
# 返回值中包含函数名（不修改函数的调用方式）

def get_func_id(func):
    print('function location: ', func);
    return func;

def test_1():
    print('hello world');

# 所有的函数无论怎么赋值 都指向同一块地址，因为代码是一样的
print('initial function location: ', test_1)
print('function location(return from function): ', get_func_id(test_1))



# 闭包
# 隐藏内部方法&内部属性&变量
def fun_closure(a, b):
    add = a + b;
    mul = a * b;
    def inner_fun():
        print('inner function called', add, mul);
    return inner_fun;

inner_fun = fun_closure(10, 20);
inner_fun()


#---------------------------------------------
# 装饰器最终版本
def final_decorator(type): # 处理装饰器传入参数
    def deal_diff_fun(func): # 接受函数地址
        def wrapper(*arg, **kwarg): # 处理函数参数
            if type == 'name':
                print('call name method');
            elif type == 'age': # 如果是年龄的话+1
                print('call age method');
                arg = (arg[0]+1,)
            ret_func = func(*arg, **kwarg);
            print('finished!')
            return ret_func;
        return wrapper;
    return deal_diff_fun;

@final_decorator(type='name')
def tester_name(name):
    print('hello ', name)

@final_decorator(type='age')
def tester_age(age):
    print('age ', age)

tester_name('elan')
tester_age(22)