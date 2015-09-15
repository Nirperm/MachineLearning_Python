"""
73. 学習
72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．
"""

import numpy as np
from section_72 import load_txt
from section_72 import stem
from section_72 import create_feature
from sklearn import linear_model


def modelize(feature):
    word_list = feature.data  # 10661
    label = feature.target  # 10661

    pos_vec = np.zeros(len(word_list))
    neg_vec = np.zeros(len(word_list))

    for i, l in enumerate(label):
        if l == 1:
            pos_vec[i] += 1
        else:
            neg_vec[i] += 1
    logreg = linear_model.LogisticRegression(penalty='l2',
                                             dual=False,
                                             tol=0.0001,
                                             C=1.0,
                                             fit_intercept=True,
                                             intercept_scaling=1,
                                             class_weight=None,
                                             random_state=None,
                                             solver='liblinear',
                                             max_iter=100,
                                             multi_class='ovr',
                                             verbose=0)
    logreg.fit([pos_vec, neg_vec], [1, -1])
    return logreg


if __name__ == '__main__':
    lines = load_txt()
    stems = stem(lines)
    feature = create_feature(lines, stems)
    logreg = modelize(feature)
    print(logreg)
