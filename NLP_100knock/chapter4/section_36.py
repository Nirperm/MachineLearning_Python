"""
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，
出現頻度の高い順に並べよ．
"""

from section_30 import load_txt
from section_30 import analyze
from section_30 import dictnize


def calc_tf(morph_dics):
    """ tfを計算する """
    tf = {}
    for x in morph_dics:
        if x['surface'] in tf:
            tf[x['surface']] = tf[x['surface']] + 1
        else:
            tf[x['surface']] = 1

    return tf


if __name__ == '__main__':
    txt = load_txt('./data/neko.txt')
    morph = analyze(txt)
    tf = calc_tf(dictnize(morph))
    sorted_tf = reversed(sorted(tf.items(), key=lambda x: x[1]))
    for k, v in sorted_tf:
        print(k)
