"""
96. 国名に関するベクトルの抽出
word2vecの学習結果から，国名に関するベクトルのみを抜き出せ．
"""

import pickle
from gensim.models import word2vec

dic = dict()
model = word2vec.Word2Vec.load_word2vec_format('data/fb_post.bin', binary=True)
for line in open('../chapter9/data/countries.txt'):
    word = line.strip()
    if model.__contains__(word):
        dic[word] = model[word]
pickle.dump(dic, open('data/countries.pkl', 'wb'))
