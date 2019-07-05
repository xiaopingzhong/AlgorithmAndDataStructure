#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-04 21:51
@Author  : zxp
@Project : tensorflow-resnet
@File    : Show-Show.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""
import os
import sys

import cv2
import numpy as np
import tensorflow as tf

from image_processing import image_preprocessing
from Appendix.残差网络 import inference

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('model_save_dir', '/data/zxp/Pretrain_model/resNet',
                           """Directory where to write event logs """
                           """and checkpoint.""")
tf.app.flags.DEFINE_integer('batch_size', 1, "batch size")
tf.app.flags.DEFINE_boolean('resume', True,
                            'resume from latest saved state')
tf.app.flags.DEFINE_string('test_dir', "/data/zxp/tensorflow_reNet/cut_result", '')


def main(filepath):
    with tf.get_default_graph().as_default():
        one_image_place = tf.placeholder(shape=[None, None, None, 3], dtype=tf.float32)
        one_label_place = tf.placeholder(shape=[None,], dtype=tf.int64)
        global_step = tf.get_variable('global_step', [],
                                      initializer=tf.constant_initializer(0),
                                      trainable=False)

        # model predict
        logits = inference(one_image_place,
                           num_classes=2,
                           is_training=False,
                           bottleneck=False,
                           num_blocks=[2, 2, 2, 2])

        predictions = tf.nn.softmax(logits)
        predict_label = tf.argmax(predictions, 1)
        correct_prediction = tf.equal(tf.argmax(predictions, 1), one_label_place)
        test_acc = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        i = [test_acc, logits, predictions, one_label_place, predict_label, correct_prediction]

        init = tf.initialize_all_variables()

        saver = tf.train.Saver(tf.all_variables())

        sess_config = tf.ConfigProto(allow_soft_placement=True)
        sess_config.gpu_options.allow_growth = True

        with tf.Session(config=sess_config) as sess:
            sess.run(init)


            if FLAGS.resume:
                latest = tf.train.latest_checkpoint(FLAGS.model_save_dir)
                if not latest:
                    print("No checkpoint to continue from in", FLAGS.model_save_dir)
                    sys.exit(1)
                print("resume", latest)
                saver.restore(sess, latest)
            global step
            step = int(sess.run(global_step))
            # test_length=len(os.listdir(filepath))
            test_acc_l, logits_l, predictions_l, one_label_place_l, predict_label_l, correct_prediction_l=[],[],[],[],[],[],
            # for x in range(int(test_length / FLAGS.batch_size)):
            sum_result_l, image_name_l = distorted_inputs(filepath, sess)
            for one_result in sum_result_l:
                one_image_tensor = one_result[0]
                one_label_tensor = one_result[1]
                one_image_np, one_label_np = sess.run([one_image_tensor, one_label_tensor])

                feed_dict = {one_image_place: one_image_np, one_label_place: one_label_np}
                test_acc, logits, predictions, one_label_value, predict_label, correct_prediction = sess.run(i,
                                                                                                             feed_dict=feed_dict)

                test_acc_l.append(test_acc)
                logits_l.append(logits)
                predictions_l.append(predictions)
                one_label_place_l.append(one_label_value)
                predict_label_l.append(predict_label)
                correct_prediction_l.append(correct_prediction)

            metric(image_name_l, test_acc_l, logits_l, predictions_l, one_label_place_l, predict_label_l, correct_prediction_l)


def metric(image_name_l, test_acc=None, logits=None, predictions=None, one_label_place=None, predict_label=None,
           correct_prediction=None):
    """
    计算各项指标
    :param image_name_l:
    :param test_acc:
    :param logits:
    :param predictions:
    :param one_label_place:
    :param predict_label:
    :param correct_prediction:
    :return:
    """
    summary_correct_true = 0
    summary_correct_false = 0
    one_count_l = []
    zero_count_l = []
    one_count = 0
    zero_count = 0
    location = 0
    error_judge_l = []

    # start_time = time.time()
    print("打印准确率:")
    print(test_acc)
    print("模型计算概率:")
    print(logits)
    print("归一化概率:")
    print(predictions)
    print("判断标签")
    print(predict_label)
    print("真实标签:")
    print(one_label_place)
    print("判断结果:")
    print(correct_prediction)
    for x in correct_prediction:
        if x == True:
            summary_correct_true += 1
        else:
            summary_correct_false += 1
            error_judge = image_name_l[location]
            error_judge_l.append(error_judge)
        location += 1
    for p, q in zip(one_label_place, predict_label):
        if p == 1:
            one_count += 1
            if p == q:
                one_count_l.append(q)
        if p == 0:
            zero_count += 1
            if p == q:
                zero_count_l.append(q)
    # duration = time.time() - start_time
    print("打印步数:")
    print(step)

    accurrancy = summary_correct_true / (summary_correct_false + summary_correct_true)
    print("打印总准确率:")

    print("正确个数为:{}".format(summary_correct_true))
    print("错误个数为:{}".format(summary_correct_false))
    print("总准确率为:{}".format(accurrancy))

    one_acc = len(one_count_l) / one_count
    zero_acc = len(zero_count_l) / zero_count

    print("ACC:")
    print("one_amount: {},one_acc: {}".format(one_count, one_acc))
    print("zero_amount: {},zero_acc: {}".format(zero_count, zero_acc))
    print("\n")
    print("print the judge error picture:")
    print(error_judge_l)
    for x in error_judge_l:
        img = cv2.imread(x)
        cv2.imwrite(os.path.join("/data/zxp/tensorflow_reNet/error_judge_image", os.path.basename(x)), img)
    print(len(error_judge_l))
    with open("/data/zxp/tensorflow_reNet/Metric.txt", mode="w") as  f:
        f.write("一.打印总准确率:\n")
        f.write("正确个数为:{}\n".format(summary_correct_true))
        f.write("错误个数为:{}".format(summary_correct_false))
        f.write("总准确率为:{}\n\n".format(accurrancy))
        f.write("二.ACC:\n")
        f.write("one_amount: {},one_acc: {}\n".format(one_count, one_acc))
        f.write("zero_amount: {},zero_acc: {}\n\n".format(zero_count, zero_acc))
        f.write("三.判断错误图片的长度为:{},各个图片的名称为:\n".format(len(error_judge_l)))
        f.write("\n".join(error_judge_l))


def load_data(file_path):
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


def distorted_inputs(filepath,sess):
    """
    对图片进行预处理
    :param filepath:
    :param sess:
    :return:
    """
    image_l, label_l = load_data(filepath)
    # print("打印image_l")
    # print(image_l,label_l)
    # exit(1)
    # 路径是二进制
    filename, label_index = tf.train.slice_input_producer([image_l, label_l], shuffle=False)
    coord = tf.train.Coordinator()
    # 新建一个数据导入的线程,并且交由线程管理器coord管理
    tf.train.start_queue_runners(sess=sess, coord=coord)

    sum_result_l=[]
    for x in range(len(os.listdir(filepath))):
        image_buffer = tf.read_file(filename)
        bbox = []
        train = False
        image = image_preprocessing(image_buffer, bbox, train, sess)
        image = tf.cast(image, tf.float32)
        # Tensor("Reshape:0", shape=(1, 32, 950, 3), dtype=float32)
        one_image = tf.expand_dims(image, 0)
        # ("Reshape_1:0", shape=(1,), dtype=int64)
        one_label=tf.reshape(label_index, [FLAGS.batch_size])
        sum_result_l.append([one_image,one_label])
        # yield one_image,one_label,image_l
    return sum_result_l,image_l


if __name__ == '__main__':
    filepath = FLAGS.test_dir
    main(filepath)
