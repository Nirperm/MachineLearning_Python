"""
38.ヒストグラム
単語の出現頻度のヒストグラム
（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）
を描け．
"""

import matplotlib
matplotlib.use('Agg')
import math
import matplotlib.pyplot as plt
import numpy as np
from section_30 import load_txt
from section_30 import analyze
from section_30 import dictnize
from section_36 import calc_tf


def make_hist(sorted_tf):
    """ ヒストグラム作成に必要な値を計算する """

    tf_histgram = {}
    for x in sorted_tf:
        if x[1] in tf_histgram:
            tf_histgram[x[1]] = tf_histgram[x[1]] + 1
        else:
            tf_histgram[x[1]] = 1

    return tf_histgram


def plot_hist(tf_histgram):
    frequency_list = []
    category_list = []

    for key, value in tf_histgram.items():
        category_list.append(key)
        frequency_list.append(value)

    data = np.array([category_list, frequency_list]).T

    # fixed number of bins
    """
    bins = np.linspace(math.ceil(min(data)),
                       math.floor(max(data)),
                       20)
    plt.xlim([min(data) - 5, max(data) + 5])
    """
    plt.hist(data, bins=50, normed=False, facecolor='b', alpha=0.8)
    plt.title('Histogram', size=16)
    plt.xlabel('Frequency', size=14)
    plt.ylabel('The number of type', size=14)
    plt.savefig('data/38.png')


if __name__ == '__main__':
    txt = load_txt('./data/neko.txt')
    morph = analyze(txt)
    tf = calc_tf(dictnize(morph))
    sorted_tf = sorted(tf.items(), key=lambda x: x[1], reverse=True)
    tf_histgram = make_hist(sorted_tf)
    plot_hist(tf_histgram)
