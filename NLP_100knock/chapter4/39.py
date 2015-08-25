"""
39. Zipfの法則 (右肩下がりの図)
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
(ジップの法則とは、出現頻度がk番目に大きい要素が全体に占める割合が1/kに比例するという経験則)

# refer http://naga0001.at.webry.info/201412/article_1.html
"""

import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from section_30 import load_txt
from section_30 import analyze
from section_30 import dictnize
from section_36 import calc_tf


def zipf(tf_dict):
    x = np.array([key for key in tf_dict.keys()])
    y = np.array([value for value in tf_dict.values()])
    plt.title('Zipf', size=16)
    plt.xlabel('Log(Rank)', size=14)
    plt.ylabel('Frequency', size=14)

    plt.loglog(x, y)
    plt.xlim([0, max(x)])
    plt.ylim([0, max(y)])

    plt.savefig('data/39.png')

if __name__ == '__main__':
    txt = load_txt('./data/neko.txt')
    morph = analyze(txt)
    tf = calc_tf(dictnize(morph))
    sorted_tf = sorted(tf.items(), key=lambda x: x[1], reverse=True)

    rank_tf = {}
    for i, ele in enumerate(sorted_tf):
        rank_tf[i + 1] = ele[1]
    zipf(rank_tf)
