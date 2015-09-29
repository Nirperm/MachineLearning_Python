"""
88. 類似度の高い単語10件
85で得た単語の意味ベクトルを読み込み，
"England"とコサイン類似度が高い10語と，その類似度を出力せよ．
"""

import pickle
import numpy


def cossim(x, y):
    return numpy.sum(x * y) / (numpy.sqrt(numpy.sum(x * x)) * numpy.sqrt(numpy.sum(y * y)))


def similer_words(query, Xpca, word2id, n=10):
    query_id = word2id[query]
    id2word = {v: k for k, v in word2id.items()}
    query_v = Xpca[query_id]
    similers = list()
    for i, v in enumerate(Xpca):
        if i == query_id:
            continue
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
    query = 'England'
    print('query: England')
    for w, v, s in similer_words(query, Xpca, word2id):
        print(w, s)
