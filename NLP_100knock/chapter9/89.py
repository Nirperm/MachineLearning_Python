"""
89. 加法構成性によるアナロジー
85で得た単語の意味ベクトルを読み込み，
vec("Spain") - vec("Madrid") + vec("Athens")を計算し，
そのベクトルと類似度の高い10語とその類似度を出力せよ．
"""

import pickle
import numpy


def cossim(x, y):
    return numpy.sum(x * y) / (numpy.sqrt(numpy.sum(x * x)) * numpy.sqrt(numpy.sum(y * y)))


def similer_words(query_v, Xpca, word2id, n=10):
    id2word = {v: k for k, v in word2id.items()}
    similers = list()
    for i, v in enumerate(Xpca):
        if len(similers) < n:
            similers.append((id2word[i], v, cossim(v, query_v)))
            similers = sorted(similers, key=lambda x: -x[2])
        else:
            new_sim = cossim(v, query_v)
            for j, (_, _, sim) in enumerate(similers):
                if sim < new_sim:
                    similers.pop(j)
                    similers.insert(j, (id2word[i], v, new_sim))
                    break
    return similers


if __name__ == '__main__':
    Xpca = pickle.load(open('data/Xpca.pkl', 'rb'))
    word2id = pickle.load(open('data/word2id.pkl', 'rb'))

    spain = Xpca[word2id['Spain']]
    madrid = Xpca[word2id['Madrid']]
    athens = Xpca[word2id['Athens']]
    query = spain - madrid + athens
    print('query: Spain - Madrid + Athens')
    for w, v, s in similer_words(query, Xpca, word2id):
        print(w, s)
