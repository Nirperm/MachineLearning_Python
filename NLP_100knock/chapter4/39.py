"""
39. Zipfの法則 (右肩下がりの図)
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""
# refer http://naga0001.at.webry.info/201412/article_1.html

import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from section_30 import load_txt
from section_30 import analyze
from section_30 import dictnize
from section_36 import calc_tf
from section_38 import count_word


def zipf(tf_histgram):
    frequency_list = []
    category_list = []
    zipf_list = []
    for key, value in tf_histgram.items():
        category_list.append(key)
        frequency_list.append(value)
        zipf_list.append(key * value)

    x = np.array(zipf_list)
    y = np.log(x)

    plt.title('Zipf', size=16)
    plt.xlabel('Log(rank)', size=14)
    plt.ylabel('Frequency', size=14)

    plt.plot(x, y)
    plt.savefig('data/39.png')
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(0, len(word_list))
    ax.set_ylim(0, len(count_list))

    x = np.array(count_list)
    y = np.sin(2 * np.pi * x)
    x[np.isnan(x)] = np.nanmean(x)
    y[np.isnan(y)] = np.nanmean(y)
    plt.loglog(x, y)
    plt.savefig('data/39.png')
    """

if __name__ == '__main__':
    txt = load_txt('./data/neko.txt')
    morph = analyze(txt)
    tf = calc_tf(dictnize(morph))
    sorted_tf = sorted(tf.items(), key=lambda x: x[1], reverse=True)
    tf_histgram = count_word(sorted_tf)
    zipf(tf_histgram)
