"""
74. 予測
73で学習したロジスティック回帰モデルを用い，
与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，
その予測確率を計算するプログラムを実装せよ．
"""

import numpy as np
import itertools
from section_72 import load_txt
from section_72 import stem
from section_72 import create_feature
from section_73 import modelize


def predict(logreg, feature):
    sentence = 'rodriguez . . . was unable to reproduce the special spark between the characters that made the first film such a delight .'.split()  #=> label is -1(neg)
    input_vec = np.zeros(len(feature.data))

    nested_stem = stem(sentence)  # stemed word list in nested list
    word_list = list(itertools.chain.from_iterable(nested_stem))

    index = feature.data.index(word_list)
    input_vec[index] += 1

    print(logreg.predict(input_vec))
    print(logreg.predict_proba(input_vec))

if __name__ == '__main__':
    lines = load_txt()
    stems = stem(lines)
    feature = create_feature(lines, stems)
    logreg = modelize(feature)
    predict(logreg, feature)
