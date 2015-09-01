"""
76. ラベル付け
学習データに対してロジスティック回帰モデルを適用し，
正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．
"""

import math
# import os
import re
# import sys
# sys.path.append('/home/vagrant/libsvm-3.20/python/')
import numpy as np
from section_72 import load_txt
from section_72 import stem
from section_72 import create_feature
from section_75 import create_dict

# from section_73 import modelize
# from svm import *
# from svmutil import *


if __name__ == '__main__':
    lines = load_txt()
    stems = stem(lines)
    feature = create_feature(lines, stems)
    # logreg = modelize(feature)
    # data = feature.data

    label = feature.target
    dictionary = create_dict(stems)  # key is id, value is stemming word

    keys = [key for key in dictionary.keys()]

    """
    ids = []  # feature id
    values = []  # feature value
    labels = []  # feature label
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
    """

    # regulation of Cosine
    """
    values = values / np.linalg.norm(values)
    val = sum(values)
    print(math.exp(-val))
    print(1.0 / (1.0 + math.exp(-val)))
    # print(len([1.0 / (1.0 + math.exp(-x)) for x in values]))
    """
