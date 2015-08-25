"""
38.ヒストグラム
単語の出現頻度のヒストグラム
（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）
を描け．
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from section_30 import load_txt
from section_30 import analyze
from section_30 import dictnize
from section_36 import calc_tf


def count_word(sorted_tf):
    """ ヒストグラム作成に必要な値を計算する """

    tf_histgram = {}
    for x in sorted_tf:
        if x[1] in tf_histgram:
            tf_histgram[x[1]] = tf_histgram[x[1]] + 1
        else:
            tf_histgram[x[1]] = 1

    return tf_histgram


def plot_hist(tf_dict):
    category_list = np.array([key for key in tf_dict.keys()])
    frequency_list = np.array([value for value in tf_dict.values()])
    # data = np.array([category_list, frequency_list]).T

    plt.title('Histogram', size=16)
    plt.xlabel('Frequency', size=14)
    plt.ylabel('The number of type', size=14)

    # plt.hist(data, bins=50, normed=False, facecolor='b', alpha=0.8)
    plt.bar(frequency_list, category_list)
    plt.xlim([0, max(frequency_list)])
    plt.ylim([0, max(category_list)])

    plt.savefig('data/38.png')


if __name__ == '__main__':
    txt = load_txt('./data/neko.txt')
    morph = analyze(txt)
    tf = calc_tf(dictnize(morph))
    sorted_tf = sorted(tf.items(), key=lambda x: x[1], reverse=True)
    category_tf = {}
    for i, ele in enumerate(sorted_tf):
        category_tf[i + 1] = ele[1]
    plot_hist(category_tf)
