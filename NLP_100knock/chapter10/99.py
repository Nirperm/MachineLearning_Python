"""
99. t-SNEによる可視化
96の単語ベクトルに対して，ベクトル空間をt-SNEで可視化せよ．
"""

import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

dic = pickle.load(open('data/countries.pkl', 'rb'))
features = [np.array(v) for v in dic.values()]

embeded = TSNE().fit_transform(features)

x, y = zip(*embeded)
for (xx, yy), key in zip(embeded, dic.keys()):
    plt.text(xx, yy, key)
plt.axis([min(x), max(x), min(y), max(y)])
plt.savefig('data/99_result.png')
