
9/2 ;  # 4.5
9//2;  # 4
9%2 ;  # 1

# 字符串分片
str = 'hello world';
str_1 = str[0:5];
str_2 = str[-5:];
#print(str_1, str_2)

# 电话隐私替换
phone = '186-1263-4669'
phone_security = phone.replace(phone[0:3], '*'*3).replace(phone[4:8], '*'*4)
#print(phone_security)

input_num = '1263'
position_s = phone.find(input_num);
position_e = phone.find(input_num)+len(input_num);
#print('phone number:', phone, 'hightlight:', position_s, position_e)

#print('the first step is print {} {}'.format('hello', 'world'));
#print('the first step is print {two} {one}'.format(one='world',two='hello'));
#iwords = input('input your words: _')
#print('your type {}'.format(iwords))

def calc_area(para1, para2) :
  if type(para1) != type(1) or type(para2) != type(2):
    print('please input integer');
  return (int(para1) * int(para2)) / 2;

#print(calc_area(10, 1));

def personal_open(file_name, msg='') :
  if file_name == '' :
    print("the file name shouldn't be empty");
    return 0 ;
  file_full_name = 'C:\\Users\\Elaner\\Desktop\\' + file_name ;
  with open(file_full_name, 'w') as fp:
    fp.write(msg);


personal_open('', msg = 'hello world');



