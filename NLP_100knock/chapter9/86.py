"""
86. 単語ベクトルの表示
85で得た単語の意味ベクトルを読み込み，"United States"のベクトルを表示せよ．
ただし，"United States"は内部的には"United_States"と表現されていることに注意せよ．
"""

import pickle

Xpca = pickle.load(open('data/Xpca.pkl', 'rb'))
word2id = pickle.load(open('data/word2id.pkl', 'rb'))

i = word2id['United_States']
print(Xpca[i])
