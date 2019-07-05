#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-05 22:32
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 残差网络.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""

import tensorflow as tf
from config import Config
from image_processing import Dynamic_width
from tensorflow.python.ops import control_flow_ops
from tensorflow.python.training import moving_averages

MOVING_AVERAGE_DECAY = 0.9997  ##滑动平均模型衰减率
BN_DECAY = MOVING_AVERAGE_DECAY  ##BN层衰减率
BN_EPSILON = 0.001
CONV_WEIGHT_DECAY = 0.00004  ##卷积层权重衰减率
CONV_WEIGHT_STDDEV = 0.1  # 卷积层权重标准差
FC_WEIGHT_DECAY = 0.00004  # #全连接层权重衰减率
FC_WEIGHT_STDDEV = 0.01
RESNET_VARIABLES = 'resnet_variables'
UPDATE_OPS_COLLECTION = 'resnet_update_ops'  # must be grouped with training op
IMAGENET_MEAN_BGR = [103.062623801, 115.902882574, 123.151630838, ]  ##图像的平均BGR

tf.app.flags.DEFINE_integer('input_size', Dynamic_width, "input image size")
tf.app.flags.DEFINE_integer('fixed_height', 32, "input image size")

activation = tf.nn.relu


def inference(x, is_training, num_classes=1000,
              num_blocks=[3, 4, 6, 3],  # defaults to 50-layer network
              use_bias=False,  # defaults to using batch norm
              bottleneck=True):
    # *********+++++++++++*********========*********+++++++++++*********========
    # 残差网络有这样几个特点：
    # 1. 网络较瘦，控制了参数数量；
    # 2. 存在明显层级，特征图个数逐层递进，保证输出特征表达能力；
    # 3. 使用了较少的池化层，大量使用下采样，提高传播效率；
    # 4. 没有使用Dropout，利用BN和全局平均池化进行正则化，加快了训练速度；
    # 5. 层数较高时减少了3x3卷积个数，并用1x1卷积控制了3x3卷积的输入输出特征图数量，称这种结构为“瓶颈”(bottleneck)
    # *********+++++++++++*********========*********+++++++++++*********========

    # 总体配置
    c = Config()
    # 配置默认参数
    c['bottleneck'] = bottleneck
    # 用于将不同数据变成张量
    c['is_training'] = tf.convert_to_tensor(is_training,
                                            dtype='bool',
                                            name='is_training')
    c['ksize'] = 3
    c['stride'] = 1
    c['use_bias'] = use_bias
    c['fc_units_out'] = num_classes
    c['num_blocks'] = num_blocks
    c['stack_stride'] = 2

    with tf.variable_scope('scale1'):
        c['conv_filters_out'] = 64
        c['ksize'] = 7
        c['stride'] = 2
        # print(x)
        # exit(1)
        x = conv(x, c)
        x = bn(x, c)
        x = activation(x)
    # 第一个残差单元输入64通道输出256通道
    with tf.variable_scope('scale2'):
        x = _max_pool(x, ksize=3, stride=2)
        c['num_blocks'] = num_blocks[0]
        c['stack_stride'] = 1
        c['block_filters_internal'] = 64
        x = stack(x, c)
    # 输入128通道，输出512
    with tf.variable_scope('scale3'):
        c['num_blocks'] = num_blocks[1]
        c['block_filters_internal'] = 128
        assert c['stack_stride'] == 2
        x = stack(x, c)

    # 输入256，输出1024
    with tf.variable_scope('scale4'):
        # 6个残差块
        c['num_blocks'] = num_blocks[2]
        c['block_filters_internal'] = 256
        x = stack(x, c)

    # 输入512，输出2048
    with tf.variable_scope('scale5'):
        c['num_blocks'] = num_blocks[3]
        c['block_filters_internal'] = 512
        x = stack(x, c)

    # post-net 平均池化
    x = tf.reduce_mean(x, reduction_indices=[1, 2], name="avg_pool")

    # 最后进行全链接层
    if num_classes != None:
        with tf.variable_scope('fc'):
            x = fc(x, c)

    return x


# This is what they use for CIFAR-10 and 100.
# See Section 4.2 in http://arxiv.org/abs/1512.03385
def inference_small(x,
                    is_training,
                    num_blocks=3,  # 6n+2 total weight layers will be used.
                    use_bias=False,  # defaults to using batch norm
                    num_classes=10):
    c = Config()
    c['is_training'] = tf.convert_to_tensor(is_training,
                                            dtype='bool',
                                            name='is_training')
    c['use_bias'] = use_bias
    c['fc_units_out'] = num_classes
    c['num_blocks'] = num_blocks
    c['num_classes'] = num_classes
    inference_small_config(x, c)


def inference_small_config(x, c):
    c['bottleneck'] = False
    c['ksize'] = 3
    c['stride'] = 1
    with tf.variable_scope('scale1'):
        c['conv_filters_out'] = 16
        c['block_filters_internal'] = 16
        c['stack_stride'] = 1
        x = conv(x, c)
        x = bn(x, c)
        x = activation(x)
        x = stack(x, c)

    with tf.variable_scope('scale2'):
        c['block_filters_internal'] = 32
        c['stack_stride'] = 2
        x = stack(x, c)

    with tf.variable_scope('scale3'):
        c['block_filters_internal'] = 64
        c['stack_stride'] = 2
        x = stack(x, c)

    # post-net
    x = tf.reduce_mean(x, reduction_indices=[1, 2], name="avg_pool")

    if c['num_classes'] != None:
        with tf.variable_scope('fc'):
            x = fc(x, c)

    return x


# #将图像的RGB数据转换为BGR数据，区间变为[0,255]
def _imagenet_preprocess(rgb):
    """Changes RGB [0,1] valued image to BGR [0,255] with mean subtracted."""
    red, green, blue = tf.split(3, 3, rgb * 255.0)
    bgr = tf.concat(3, [blue, green, red])
    bgr -= IMAGENET_MEAN_BGR
    return bgr


def loss(logits, labels):
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=labels)
    cross_entropy_mean = tf.reduce_mean(cross_entropy)

    regularization_losses = tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES)
    # 交叉熵损失和正则化损失
    loss_ = tf.add_n([cross_entropy_mean] + regularization_losses)
    tf.summary.scalar('loss', loss_)

    return loss_


# 定义堆叠block,也就是残差块的函数
def stack(x, c):
    # 残差块的个数,不断叠加
    for n in range(c['num_blocks']):
        s = c['stack_stride'] if n == 0 else 1
        c['block_stride'] = s
        with tf.variable_scope('block%d' % (n + 1)):
            x = block(x, c)
    return x


# 定义block,也就是残差块
def block(x, c):
    # 获取输入通道数(也就是上一部分的输出)
    filters_in = x.get_shape()[-1]

    # Note: filters_out isn't how many filters are outputed.
    # That is the case when bottleneck=False but when bottleneck is
    # True, filters_internal*4 filters are outputted. filters_internal is how many filters
    # the 3x3 convs output internally.

    #
    m = 4 if c['bottleneck'] else 1
    # 本层输出的卷积核的个数,也就是通道数
    filters_out = m * c['block_filters_internal']

    # 短连接
    shortcut = x  # branch 1

    # 上一个输出等于下一个输出
    c['conv_filters_out'] = c['block_filters_internal']

    # 一个残差单元的结构(1*1  3*3 1*1 )
    if c['bottleneck']:
        # 1*1 卷积
        with tf.variable_scope('a'):
            c['ksize'] = 1
            c['stride'] = c['block_stride']
            x = conv(x, c)
            x = bn(x, c)
            x = activation(x)

        with tf.variable_scope('b'):
            x = conv(x, c)
            x = bn(x, c)
            x = activation(x)

        # 1*1卷积
        with tf.variable_scope('c'):
            c['conv_filters_out'] = filters_out
            c['ksize'] = 1
            assert c['stride'] == 1
            x = conv(x, c)
            x = bn(x, c)
    # 不用残差单元(两个3*3)
    else:
        with tf.variable_scope('A'):
            c['stride'] = c['block_stride']
            assert c['ksize'] == 3
            x = conv(x, c)
            x = bn(x, c)
            x = activation(x)

        with tf.variable_scope('B'):
            c['conv_filters_out'] = filters_out
            assert c['ksize'] == 3
            assert c['stride'] == 1
            x = conv(x, c)
            x = bn(x, c)

    # 若输入输出通道不一致则再通过一个卷积层将其变一致
    with tf.variable_scope('shortcut'):
        # 短路链接
        if filters_out != filters_in or c['block_stride'] != 1:
            c['ksize'] = 1
            c['stride'] = c['block_stride']
            c['conv_filters_out'] = filters_out
            shortcut = conv(shortcut, c)
            shortcut = bn(shortcut, c)

    # #返回经过残差单元的数据
    return activation(x + shortcut)


def bn(x, c):
    x_shape = x.get_shape()
    params_shape = x_shape[-1:]

    if c['use_bias']:
        bias = _get_variable('bias', params_shape,
                             initializer=tf.zeros_initializer)
        return x + bias

    axis = list(range(len(x_shape) - 1))

    beta = _get_variable('beta',
                         params_shape,
                         initializer=tf.zeros_initializer)
    gamma = _get_variable('gamma',
                          params_shape,
                          initializer=tf.ones_initializer)

    moving_mean = _get_variable('moving_mean',
                                params_shape,
                                initializer=tf.zeros_initializer,
                                trainable=False)
    moving_variance = _get_variable('moving_variance',
                                    params_shape,
                                    initializer=tf.ones_initializer,
                                    trainable=False)

    # These ops will only be preformed when training.
    mean, variance = tf.nn.moments(x, axis)
    update_moving_mean = moving_averages.assign_moving_average(moving_mean,
                                                               mean, BN_DECAY)
    update_moving_variance = moving_averages.assign_moving_average(
        moving_variance, variance, BN_DECAY)
    tf.add_to_collection(UPDATE_OPS_COLLECTION, update_moving_mean)
    tf.add_to_collection(UPDATE_OPS_COLLECTION, update_moving_variance)

    mean, variance = control_flow_ops.cond(
        c['is_training'], lambda: (mean, variance),
        lambda: (moving_mean, moving_variance))

    x = tf.nn.batch_normalization(x, mean, variance, beta, gamma, BN_EPSILON)
    # x.set_shape(inputs.get_shape()) ??

    return x


def fc(x, c):
    num_units_in = x.get_shape()[1]
    num_units_out = c['fc_units_out']
    weights_initializer = tf.truncated_normal_initializer(
        stddev=FC_WEIGHT_STDDEV)

    weights = _get_variable('weights',
                            shape=[num_units_in, num_units_out],
                            initializer=weights_initializer,
                            weight_decay=FC_WEIGHT_STDDEV)
    biases = _get_variable('biases',
                           shape=[num_units_out],
                           initializer=tf.zeros_initializer)
    x = tf.nn.xw_plus_b(x, weights, biases)
    return x


# 做一个l2regularizer和加入collections
def _get_variable(name,
                  shape,
                  initializer,
                  weight_decay=0.0,
                  dtype='float',
                  trainable=True):
    "A little wrapper around tf.get_variable to do weight decay and add to"
    "resnet collection"
    if weight_decay > 0:
        regularizer = tf.contrib.layers.l2_regularizer(weight_decay)
    else:
        regularizer = None
    collections = [tf.GraphKeys.VARIABLES, RESNET_VARIABLES]
    return tf.get_variable(name,
                           shape=shape,
                           initializer=initializer,
                           dtype=dtype,
                           regularizer=regularizer,
                           collections=collections,
                           trainable=trainable)


def conv(x, c):
    ksize = c['ksize']
    stride = c['stride']
    filters_out = c['conv_filters_out']

    filters_in = x.get_shape()[-1]
    shape = [ksize, ksize, filters_in, filters_out]
    initializer = tf.truncated_normal_initializer(stddev=CONV_WEIGHT_STDDEV)
    weights = _get_variable('weights',
                            shape=shape,
                            dtype='float',
                            initializer=initializer,
                            weight_decay=CONV_WEIGHT_DECAY)
    return tf.nn.conv2d(x, weights, [1, stride, stride, 1], padding='SAME')


def _max_pool(x, ksize=3, stride=2):
    return tf.nn.max_pool(x,
                          ksize=[1, ksize, ksize, 1],
                          strides=[1, stride, stride, 1],
                          padding='SAME')
