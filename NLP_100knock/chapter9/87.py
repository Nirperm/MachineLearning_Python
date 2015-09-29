"""
87. 単語の類似度
85で得た単語の意味ベクトルを読み込み，"United States"と"U.S."のコサイン類似度を計算せよ．
ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．
"""

import pickle
import numpy


def cossim(x, y):
    return numpy.sum(x * y) / (numpy.sqrt(numpy.sum(x * x)) * numpy.sqrt(numpy.sum(y * y)))

Xpca = pickle.load(open('data/Xpca.pkl', 'rb'))
word2id = pickle.load(open('data/word2id.pkl', 'rb'))

i = word2id['United_States']
ii = word2id['U.S']

print(cossim(Xpca[i], Xpca[ii]))
