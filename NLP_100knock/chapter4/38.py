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
from section_30 import make_mecab_data
from section_37 import count_word


def main(word_count_dict):
    word_list = []
    count_list = []

    for key, value in word_count_dict.items():
        word_list.append(key)
        count_list.append(value)

    duplicated_list = list(set(x for l in word_list for x in l))

    r = np.array(count_list)
    # fixed number of bins
    bins = np.linspace(math.ceil(min(r)),
                       math.floor(max(r)),
                       20)
    plt.xlim([min(r)-5, max(r)+5])

    bar_width = 200
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(r, bins=bins, range=(0, len(count_list)), normed=False, facecolor='b', alpha=0.8, width=bar_width)
    ax.set_xlim(0, len(count_list))
    ax.set_ylim(0, len(duplicated_list))
    ax.set_title('Histogram', size=16)
    ax.set_xlabel('Frequency', size=14)
    ax.set_ylabel('The number of type', size=14)
    plt.savefig('data/38.png')


if __name__ == '__main__':
    mecab_dict_list = make_mecab_data()
    word_count_dict = count_word(mecab_dict_list)
    main(word_count_dict)
