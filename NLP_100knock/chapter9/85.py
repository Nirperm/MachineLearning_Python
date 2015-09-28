"""
85. 主成分分析による次元圧縮
84で得られた単語文脈行列に対して，主成分分析を適用し，
単語の意味ベクトルを300次元に圧縮せよ．
"""

import pickle
import sklearn.decomposition

dim = 300
X = pickle.load(open('data/X.pkl', 'rb'))
pca = sklearn.decomposition.PCA(dim)
Xpca = pca.fit_transform(X.toarray())
print(Xpca)
pickle.dump(Xpca, open('data/Xpca.pkl', 'wb'))
