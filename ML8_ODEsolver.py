# refer
# 多元一阶
# https://blog.csdn.net/weixin_41582053/article/details/110352227
# 一元多阶
# https://blog.csdn.net/MarkovDPs/article/details/120604356

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.compat.v1.disable_eager_execution()

import matplotlib.pyplot as plt
import numpy as np
import math

m1=191.4*9.8
m2=192.6*9.8
k1=7*1e4
k2=7*1e5
c1=240
c2=3500
w=201
F0=3000

x_train = np.linspace(0, 2.5, 1000, endpoint=True)#生成[0,2]区间400个点
x_t = np.zeros((len(x_train), 1))
for i in range(len(x_train)):
    x_t[i] = x_train[i]
x_tv = tf.placeholder("float", [None, 1])
# 共享层
W = tf.Variable(tf.zeros([1, 10]))
b = tf.Variable(tf.zeros([10]))
y_mid = tf.nn.sigmoid(tf.matmul(x_tv, W)+b)#sigmoid激活函数y_mid的形状[10,10]
# 各自单独层
W1 = tf.Variable(tf.zeros([10, 1]))
W2 = tf.Variable(tf.zeros([10, 1]))
b1 = tf.Variable(tf.zeros([1]))
b2 = tf.Variable(tf.zeros([1]))
x1 = tf.matmul(y_mid, W1)+b1#网络的输出[10,1]
x2 = tf.matmul(y_mid, W2)+b2#网络的输出[10,1]
# 求导
dif1_1 = tf.matmul(tf.multiply(y_mid*(1-y_mid),W),W1)#dy/dx,dif形状[100,1],即对应点的一阶导数值
dif2_1 = tf.matmul(tf.multiply((y_mid*(1-y_mid)*(1-y_mid)-y_mid*y_mid*(1-y_mid))*W, W),W1)#对应点的二阶导数值
dif1_2 = tf.matmul(tf.multiply(y_mid*(1-y_mid),W),W2)#dy/dx,dif形状[100,1],即对应点的一阶导数值
dif2_2 = tf.matmul(tf.multiply((y_mid*(1-y_mid)*(1-y_mid)-y_mid*y_mid*(1-y_mid))*W, W),W2)#对应点的二阶导数值
# loss
de1 =(m2)*dif2_2+(c2)*dif1_2+(k1)*x2-c2*dif1_1-k2*x1
de2 =(m1)*dif2_1+(c1+c2)*dif1_1+(k1+k2)*x1-c2*dif1_2-k2*x2-F0*tf.sin(w*x_tv)
t_loss = de1**2+de2**2
loss = tf.reduce_mean(t_loss)+(x1[0]-0)**2+(x2[0]-0)**2
#Adam优化器训练网络参数
train_step = tf.train.AdamOptimizer(0.001).minimize(loss)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(10000):#训练5000次
        sess.run(train_step,feed_dict={x_tv: x_t})
        if i%50 == 0:
            total_loss = sess.run(loss,feed_dict={x_tv: x_t})
            print("loss={}".format(total_loss))
            #print(sess.run(x1[0], feed_dict={x_tv: x_t}))
    # saver = tf.train.Saver(max_to_keep=1)#保存模型，训练一次后可以将训练过程注释掉
    # saver.save(sess,'ckpt/nn.ckpt',global_step=50000)
    # saver = tf.train.Saver(max_to_keep=1)
    # model_file="ckpt/nn.ckpt-50000"
    # saver.restore(sess, model_file)
    output = sess.run(x1,feed_dict={x_tv:x_t})
    output1 = sess.run(x2,feed_dict={x_tv:x_t})
    y_output = x_train.copy()
    y_output1 = x_train.copy()
    for i in range(len(x_train)):
        y_output[i] = output[i]
        y_output1[i] = output1[i]
    fig = plt.figure("x1与x2")
    L1, = plt.plot(x_train,y_output, c = 'b')
    L2, = plt.plot(x_train,y_output1, c = 'g')
    plt.legend([L1,L2],["x1","x2"], loc='upper right')
    plt.title('Comparison of results')
    plt.show()
