# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     testEnv
   Description :
   Author :       elan
   date：          3/18/2018
-------------------------------------------------
   Change Activity:
                   3/18/2018:
-------------------------------------------------
"""

import tensorflow as tf

'''
a = tf.constant([1.0, 2.0], name="a");
b = tf.constant([3.0], name="b");
c = a+b

with tf.Session() as sess:
    print(c)
    ret = sess.run(c)
    print(ret)
'''

'''
g1 = tf.Graph();
with g1.as_default():
    v = tf.get_variable(
        "v", shape=[1], initializer=tf.zeros_initializer()
    )
    a = tf.constant([1.0], name="a")

with tf.Session(graph=g1) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope("", reuse=True):
        print(sess.run(tf.get_variable("v")))
    print('a+v=', sess.run(a + v))

g2 = tf.Graph();
with g2.as_default():
    v = tf.get_variable(
        "v", shape=[1], initializer=tf.ones_initializer()
    )
    a = tf.constant([2.0], name="a")

with tf.Session(graph=g2) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope("", reuse=True):
        print(sess.run(tf.get_variable("v")))
    print('a+v=', sess.run(a + v))
'''

#---------------------------------------------------------------------------------------

'''

# 默认graph运行 下面两个命令执行效果一样

sess = tf.Session();
with sess.as_default():
    a = tf.constant([1.0], name="a")
    b = tf.constant([1.0, 2.0], name="b")
    result = a+b
    print(result, result.eval())
    result.eval(session=sess)


with tf.Session() as sess:
    a = tf.constant([1.0], name="a")
    b = tf.constant([1.0, 2.0], name="b")
    print(sess.run(a + b))
    
'''

#---------------------------------------------------------------------------------------

# 使用默认session & 配置session参数
# allow_soft_placement GPU资源放在CPU上(运行不在GPU上 / 没有GPU资源 / 预算结果包含CPU计算结果的引用
# )
# log_device_placement 启用log
'''
default_config = tf.ConfigProto(allow_soft_placement=True,
                                log_device_placement=True);
sess = tf.InteractiveSession(config=default_config)
a = tf.constant([1.0], name="a")
b = tf.constant([1.0, 2.0], name="b")
result = a + b
print(result.eval())
sess.close()
'''


#coding=utf-8
#对于单机单卡，可以把参数和计算都定义在gpu上，不过如果参数模型比较大，显存不足等情况，就得放在cpu上
import  tensorflow as tf

with tf.device('/cpu:0'):  # 将定义放到cpu上
  w = tf.get_variable('w1', (2,2), tf.float32, initializer=tf.constant_initializer(2)) # 定义w 初始化值2 二维
  b = tf.get_variable('b2', (2,2), tf.float32, initializer=tf.constant_initializer(5)) # 定义b 初始化值5 二维

with tf.device('/gpu:0'):  # 将计算放在gpu上
  addwb = w + b
  mutwb = w * b

with tf.Session() as sess:
  tf.global_variables_initializer().run()  # 如果没有初始化w1, b2的话直接使用 会报Attempting to use uninitialized value w1
  # 查看w, b对应的值
  with tf.variable_scope("", reuse=True) :  # 否则会报: Variable w1 already exists, disallowed. 因为它会再去生产一个w1
    print(sess.run([tf.get_variable('w1'), tf.get_variable('b2')]))
  print(w, b)
  np1, np2 = sess.run([addwb, mutwb])  # 运行flow(addwb, mutwb)
  print(np1)
  print(np2)

