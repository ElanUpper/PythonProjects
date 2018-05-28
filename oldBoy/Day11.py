# author: elan


import random

# 随机整数
print('random'.center(100, '-'))
print(random.randint(1, 7))  # Return random integer in range [a, b]
# 随机偶数
print(random.randrange(0, 101, 2)); # Return random integer from range(start, stop[, step])
# 随机浮点数
print(random.random()) # 随机0~1浮点数
print(random.uniform(1, 10)) # 1~10

print(random.choice('hello')); # 从制定string中选取元素返回
print(random.choice([x for x in 'hello'])); # 从制定list中选取元素返回
print(random.sample([x for x in 'hello'], 3)); # 从制定list中选取3个元素返回
# 随机洗牌功能
order_list = [1, 2, 3, 4, 5, 6];
print('before shuffle:', order_list);
random.shuffle(order_list)
print('after shuffle:', order_list);

# 返回4位验证码
check_code = '';
for i in range(4):
    curr_numb = random.randint(0, 9); # 0 - 9
    if curr_numb in range(2):
        check_code += str(chr(random.randint(65, 90))); # 大写字母
    elif curr_numb in [2, 3]:
        check_code += str(chr(random.randint(97, 122))); # 小写字母
    else :
        check_code += str(random.randint(0,9)); # 数字

print(check_code);

