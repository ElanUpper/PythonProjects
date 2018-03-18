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

a = tf.constant([1.0, 2.0], name="a");
b = tf.constant([3.0], name="b");
c = a+b

with tf.Session() as sess:
	print(c)
	ret = sess.run(c)
	print(ret)