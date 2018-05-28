# author: elan

dictStu = {
    'name'   :   'elan',
    'age'    :   23,
    'gender' :   'man'
}

print(dictStu)
# insert or update
dictStu['level'] = 'senior' ;
# get
#print('key name:' + dictStu['name1'] ); # 没有就会 报错
print('name' in dictStu) # 判断是否存在  dictStu.has_key() in python2.x
print('key name:' + dictStu.get('name') ); # 推荐写法
# delete
del dictStu['gender']
dictStu.pop('age')  # popitem 随机删除
# print all
print(dictStu)


nestedDict = {
    "China" : {
        "Alibaba" : ["taobao", "alipay"] ,
        "Baidu" : ["search engine", "cloud storage"] ,
        "Tecent" : ["QQ", "WeChat"] ,
    },
    "Germany" : {
        "SAP" : ["famous about ERP", "super technical company"]
    }
}
# print all company in china and theirs's products
print(nestedDict.get("China").keys(), nestedDict["China"].values())
# update SAP's first product
nestedDict.get("Germany").get("SAP")[0] = 'update!'
print(nestedDict.get("Germany"))


# 快速初始化 dict
# 如果初始化的值中有复杂类型 比如字典此采用的公用一块地址 也就是说修改一个值 其他都会有变化
dict1 = dict.fromkeys([1, 3, 2, 4, 5], "init")
print(dict1, '\n items:\t', dict1.items())
print('after update!!')
dict2 = {1:'upd', 4:'upd'}
dict1.update(dict2);
print(dict1, '\n items:\t', dict1.items())
# 对于负责类型
dict3 = dict.fromkeys([1,2,3], ['hello', {'key1':'cuicui', 'key2':'elan'}, 10])
print(dict3)
# 我们修改dict中key=1 对应list为key1的值  我们会发现不仅仅是key=1变化了 其他的都变化了
dict3.get(1)[1]['key1'] = 'jade';
print(dict3)