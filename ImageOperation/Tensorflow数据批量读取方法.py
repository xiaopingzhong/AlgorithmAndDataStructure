#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-05 22:24
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : Tensorflow数据批量读取方法.py
@Description: ==================================
    Tensorflow 数据批量读取方法
@license: (C) Copyright 2013-2019.    
************************************************
"""

import os

import numpy as np
import tensorflow as tf
from tensorflow.python.ops.gen_image_ops import decode_jpeg
from Appendix.残差网络 import inference

# *********+++++++++++*********========*********+++++++++++*********========
# https://blog-1-1256491104.cos.ap-chengdu.myqcloud.com/20180531141829359.gif
# https://www.cnblogs.com/demian/p/8005407.html
# http://zangbo.me/2017/07/05/TensorFlow_9/
# *********+++++++++++*********========*********+++++++++++*********========


FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('test_dir', "/data/zxp/tensorflow_reNet/cut_result", '说明变量的作用')


def load_data(file_path, is_random=True):
    """
    获取图片路径及其标签
    :param file_path: a sting, 图片所在目录
    :param is_random: True or False, 是否乱序
    :return:
    """
    image_list = []
    label_list = []

    pos_count = 0
    neg_count = 0

    for item in os.listdir(file_path):

        item_path = file_path + '/' + item
        item_label = item.split('_')[0]  # 文件名形如  neg_1.jpg,只需要取第一个

        if os.path.isfile(item_path):
            image_list.append(item_path)
        else:
            raise ValueError('文件夹中有非文件项.')

        if item_label == 'pos':  # 正向标记为'0'
            label_list.append(0)
            pos_count += 1
        else:  # 反向标记为'1'
            label_list.append(1)
            neg_count += 1
    print('数据集中有%d张正向图片,%d张反向图片.' % (pos_count, neg_count))

    image_list = np.asarray(image_list)
    label_list = np.asarray(label_list)

    return image_list, label_list


def DataReaderFlow(filepath):
    """
    数据读取工作流程
    :param filepath:
    :return:
    """
    # 加载普通的数据
    image_l, label_l = load_data(filepath)

    # (1)设置文件名队列---------路径是二进制,b'./data/1.jpg'
    filename, label_index = tf.train.slice_input_producer([image_l, label_l], shuffle=False, num_epochs=6)

    # 设置用户线程数--因为数据是从磁盘里读取的,因此读取的速度会比较慢,因此可以通过增加线程数,加快读取速度
    num_preprocess_threads = 4

    # 用[]来汇总 4个线程读取到文件
    images_and_labels = []

    # 设置4个线程来从硬盘当中读取数据
    for thread_id in range(num_preprocess_threads):
        # (2) 将文件从文件名队列,读到内存队列
        image_buffer = tf.read_file(filename)
        # 进行简单的处理--解码
        image = decode_jpeg(image_buffer)
        # 添加到文件的汇总列表当中
        images_and_labels.append([image, label_index])

    # (3)将内存队列的文件取出--dequeen,方便批处理,使用batch_join
    images, label_index_batch = tf.train.batch_join(
        tensors_list=images_and_labels,
        batch_size=FLAGS.batch_size,
        capacity=2 * num_preprocess_threads * FLAGS.batch_size,
        enqueue_many=False,
        allow_smaller_final_batch=True,
        dynamic_pad=True)

    # *********+++++++++++*********========*********+++++++++++*********========
    #   tensors_list=images_and_labels,---输入的张量tensor
    #   batch_size=FLAGS.batch_size---每次批处理取出的文件大小个数,也就是一个batch的个数
    #   capacity=2 * num_preprocess_threads * FLAGS.batch_size,---批处理队列的大小
    #   enqueue_many=True---
    #               不管是True和False,输出的数据格式,都是4维的--[样本数,width,height,channel]
    #               True时,Tensor_list当中到每个Tensor作为一个bacth(many不many代表batch的个数),因此--达到批处理的效果
    #               False时,把整体Tensor_list当作为一个bacth,tensor_list被認爲代表一个Batch.
    #   allow_smaller_final_batch=True---
    #               True时,当批处理队列当中的Tensor个数小于Batch_size,则会把剩余的张量进行返回.
    #               False时,则会将剩余的丢弃
    #   dynamic_pad=True---
    #               True:函数会自动将输入数据转换成统一尺寸大小
    #               False:输入数据尺寸需要事先手动统一尺寸.
    #   参考文献:
    #       http://zangbo.me/2017/07/05/TensorFlow_9/
    #       https://www.jianshu.com/p/a22396a61b53?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation
    #   说明:
    #       单一文件多线程，那么选用tf.train.batch（需要打乱样本，有对应的tf.train.shuffle_batch）
    #       多线程多文件的情况，一般选用tf.train.batch_join来获取样本（打乱样本同样也有对应的tf.train.shuffle_batch_join使用）
    # *********+++++++++++*********========*********+++++++++++*********========

    # 返回取到的数据
    return images, label_index_batch


def main(filepath):
    """
    数据读取的配套流程
    :param filepath:
    :return:
    """
    file_path = FLAGS.test_dir

    # 构建模型的输入
    input_place = tf.placeholder(tf.string)

    # 设置模型输入的获取方式
    images_batch, labels_batch = DataReaderFlow(file_path)

    # 设置模型的网络--用来进行预测结果
    logits = inference(images_batch,
                       num_classes=2,
                       is_training=False,
                       bottleneck=False,
                       num_blocks=[2, 2, 2, 2])

    # 对模型结果进行处理--构建指标
    predictions = tf.nn.softmax(logits)
    predict_label = tf.argmax(predictions, 1)
    correct_prediction = tf.equal(tf.argmax(predictions, 1), labels_batch)
    test_acc = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # 便于sess.run,设置需要得到到数据---便于后期进行一步处理,例如构建模型的评价指标(其实也可以先构建好,但是比较麻烦)
    i = [test_acc, logits, predictions, labels_batch, predict_label, correct_prediction]

    # tf.train.string_input_producer定义了一个epoch变量，要对它进行初始化
    # 初始化所有局部变量
    # init = tf.local_variables_initializer()

    # (5)初始化所有变量(包括局部变量--例如epoch,是否是局部变量根据变量所在的位置)
    init = tf.initialize_all_variables()

    # 配置Session,为启动做准备--一个Session(会话)可以配置多个线程
    sess_config = tf.ConfigProto(allow_soft_placement=True)
    sess_config.gpu_options.allow_growth = True

    # 启动Session
    with tf.Session(config=sess_config) as sess:
        # (6)tf.train.slice_input_producer定义了一个num_epoch变量，要对它进行初始化
        sess.run(init)
        # (7)创建线程协调管理器
        coord = tf.train.Coordinator()
        # (8)使用start_queue_runners之后，才会开始填充队列
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)

        # (9)启动主线程,消费数据
        for x in range(20):
            test_acc, logits, predictions, labels_batch_value, predict_label, correct_prediction = sess.run(i,
                                                                                                            feed_dict={
                                                                                                                input_place: filepath})
            print(test_acc)
            print(logits)
            print(predictions)
            print(labels_batch_value)
            print(predict_label)
            print(correct_prediction)

        # (10)停止子线程(这里指的是数据读取线程)--也就是当主线程不在消费数据的时候(也就是循环了20次之后)
        coord.request_stop()
        # (11)等待所有的 数据读取子线程停止,之后返回主线程Session
        coord.join(threads)


if __name__ == '__main__':
    filepath = FLAGS.test_dir
    tf.app.run(main=main(filepath))
