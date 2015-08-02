"""
73. 学習
72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．
"""

import numpy as np
# import matplotlib.pyplot as plt
from section_72 import load_sentiment
from sklearn import linear_model

if __name__ == '__main__':
    sentiment = load_sentiment()
    X = sentiment.data
    Y = sentiment.target
    h = .02  # step size in the mesh
    logreg = linear_model.LogisticRegression(penalty="l1", C=1e5)
    logreg.fit(X, Y)

    """
    print(logreg.coef_)
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z =logreg.predict(np.c_[xx.ravel(), yy.ravel()])  10000, 2
    """
