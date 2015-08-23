"""
39. Zipfの法則 (右肩下がりの図)
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""
# refer http://naga0001.at.webry.info/201412/article_1.html
# http://soy-curd.hatenablog.com/entry/2015/07/25/151521

import matplotlib
matplotlib.use('Agg')
import platform
import numpy as np
import matplotlib.pyplot as plt
from section_30 import make_mecab_data
from section_37 import count_word


def main(word_count_dict):
    word_list = []
    count_list = []

    for key, value in word_count_dict.items():
        word_list.append(key)
        count_list.append(value)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(0, len(word_list))
    ax.set_ylim(0, len(count_list))
    ax.set_title('Zipf', size=16)
    ax.set_xlabel('Log(rank)', size=14)
    ax.set_ylabel('Frequency', size=14)

    x = np.array(count_list)
    y = np.sin(2*np.pi*x)
    x[np.isnan(x)] = np.nanmean(x)
    y[np.isnan(y)] = np.nanmean(y)
    plt.loglog(x, y)
    plt.savefig('data/39.png')


if __name__ == '__main__':
    mecab_dict_list = make_mecab_data()
    word_count_dict = count_word(mecab_dict_list)
    main(word_count_dict)
