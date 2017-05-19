##!/usr/bin/python
# coding:utf-8
__author__ = '353677403@qq.com'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import tensorflow as tf
import pickle
import numpy as np


def readData(txt_vecs_file, img_vecs_file):

    """function: read pre-trained vecs.

    Args:
        txt_vecs_file: (str).
        img_vec_file: (str).
      
    Returns:
        txt_vec_list: (list)
        img_vec_list: (list)
    """
    # with open(txt_vecs_file) as fi:
    #     for line in fi:
    #         line = line.decode('utf-8').strip()
    # with open(img_vecs_file) as fi:
    #     for line in fi:
    #         line = line.decode('utf-8').strip()
    #

    txt_vecs_list = [[1,2,3]]
    img_vecs_list = [[5,6,7]]


    return txt_vecs_list, img_vecs_list


def txt2img(txt_vecs_list, img_vecs_list):
    txt_dims_num = len(txt_vecs_list[0])
    img_dims_num = len(img_vecs_list[0])
    n_samples = len(txt_vecs_list)
    batch_size = 100
    x = tf.placeholder(tf.float32, [None, txt_dims_num])
    W = tf.Variable(tf.zeros([txt_dims_num, img_dims_num]))
    b = tf.Variable(tf.zeros([img_dims_num]))
    y = tf.nn.tanh(tf.matmul(x, W) + b)
    y_ = tf.placeholder(tf.float32, [None, img_dims_num])

    cost = tf.reduce_sum(tf.pow(y-y_, 2))/(2*n_samples)

    optimizer = tf.train.GraientDescentOptimizer()

    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        for i in range(1, n_samples/batch_size+1):
            sess.run(optimizer, feed_dict={x: txt_vecs_list[(i-1)*batch_size: i*batch_size], \
                                           y_: txt_vecs_list[(i-1)*batch_size: i*batch_size]})


