"""
76. ラベル付け
学習データに対してロジスティック回帰モデルを適用し，
正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．
"""

import math
# import os
import re
import sys
sys.path.append('/home/vagrant/libsvm-3.20/python/')
import numpy as np
from section_72 import load_txt
from section_72 import stem
from section_72 import create_feature
from section_73 import modelize
from svm import *
from svmutil import *

# FIXME: setup sys.path
# FIXME: maybe data/75.scale.model is wrong

if __name__ == '__main__':
    """
    lines = load_txt()
    stems = stem(lines)
    feature = create_feature(lines, stems)
    logreg = modelize(feature)

    data = feature.data
    label = feature.target
    """

    # 配列の初期化
    ids = []  # 素性id配列
    values = []  # 素性値配列
    labels = []
    for line in open('data/75.scale.model'):
        field = line.strip().split(' ')
        if re.search('[a-zA-Z]+', field[0]) is None:
            label = field.pop(0)
            labels.append(label)
            for feature in field:
                field2 = feature.split(':')
                ids.append(field2[0])
                values.append(field2[1])

    values = np.array(values, dtype=float)

    # コサイン正規化
    values = values / np.linalg.norm(values)
    print(math.exp(-val))
    print(1.0 / (1.0 + math.exp(-val)))
    # print(len([1.0 / (1.0 + math.exp(-x)) for x in values]))
