"""
98. Ward法によるクラスタリング
96の単語ベクトルに対して，Ward法による階層型クラスタリングを実行せよ．
さらに，クラスタリング結果をデンドログラムとして可視化せよ．
"""

import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import pdist

dic = pickle.load(open('data/countries.pkl', 'rb'))
features = [np.array(v) for v in dic.values()]
labels = [v for v in dic.keys()]

model = linkage(pdist(features))
dendrogram(model, labels=labels, orientation='right')  # FIXME: more clealry
plt.savefig('data/98_result.png')
