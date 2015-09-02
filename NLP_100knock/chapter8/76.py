"""
76. ラベル付け
学習データに対してロジスティック回帰モデルを適用し，
正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．
"""

import math
import re
from section_72 import load_txt
from section_72 import stem
from section_75 import create_dict


def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))


def probability(feature_dict, keys):
    return sigmoid(sum(feature_dict.get(k, 0) for k in keys))


def predict(prob, thresh):
    return '-1' if prob < thresh else '+1'


def attach_label(keys):
    f = open('data/76.txt', 'w')
    for line in open('data/75.scale.model'):
        field = line.strip().split(' ')
        if re.search('[a-zA-Z]+', field[0]) is None:
            label = field.pop(0)
            feature_dict = dict(map(int, x.split(':')) for x in field)
            prob = probability(feature_dict, keys)

            f.write(label + ' ' + predict(prob, 0.5) + ' ' + str(prob) + '\n')
            print(label + '\t', predict(prob, 0.5), '\t', prob)
    f.close()

if __name__ == '__main__':
    lines = load_txt()
    stems = stem(lines)

    dictionary = create_dict(stems)  # key is id, value is stemming word
    keys = [key for key in dictionary.keys()]

    attach_label(keys)
