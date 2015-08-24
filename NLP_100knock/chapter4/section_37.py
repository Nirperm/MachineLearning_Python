"""
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""

import matplotlib
matplotlib.use('Agg')
import platform
import matplotlib.pyplot as plt
from section_30 import load_txt
from section_30 import analyze
from section_30 import dictnize
from section_36 import calc_tf


def plot(sorted_tf):
    word_list = []
    count_list = []
    for tf in sorted_tf[:10]:
        word_list.append(tf[0])
        count_list.append(tf[1])

    """ 日本語フォント対策 for Mac """
    if platform.system() == 'Darwin':
        font_prop = matplotlib.font_manager.FontProperties(fname='/Library/Fonts/Osaka.ttf')
    else:
        font_prop = matplotlib.font_manager.FontProperties(fname="/usr/share/fonts/truetype/fonts-japanese-gothic.ttf")

    bar_width = 100
    plt.bar(count_list, count_list, color='blue', width=bar_width, align='center')
    plt.xticks(count_list, word_list, fontproperties=font_prop)
    plt.savefig('data/37.png')


if __name__ == '__main__':
    txt = load_txt('./data/neko.txt')
    morph = analyze(txt)
    tf = calc_tf(dictnize(morph))
    sorted_tf = sorted(tf.items(), key=lambda x: x[1], reverse=True)
    plot(sorted_tf)
