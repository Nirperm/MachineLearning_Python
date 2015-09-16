"""
83. 単語／文脈の頻度の計測
82の出力を利用し，以下の出現分布，および定数を求めよ．

f(t,c): 単語tと文脈語cの共起回数
f(t,∗): 単語tの出現回数
f(∗,c): 文脈語cの出現回数
N: 単語と文脈語のペアの総出現回数
"""

import os
import pickle
from collections import Counter


def main():
    cont_count = Counter()
    word_count = Counter()
    co_occur_count = Counter()
    N = 0

    for line in open('data/82_result.txt'):
        line = line.strip().split('\t')
        word = line[0]
        cont_words = line[1:]
        word_count[word] += 1
        for cont_word in cont_words:
            N += 1
            cont_count[cont_word] += 1
            co_occur_count[word + '\t' + cont_word] += 1

    if not os.path.isfile("data/cont[].pkl"):
        pickle.dump(dict(cont_count), open('data/cont.pkl', 'wb'))

    if not os.path.isfile("data/word.pkl"):
        pickle.dump(dict(word_count), open('data/word.pkl', 'wb'))

    if not os.path.isfile("data/co_occur.pkl"):
        pickle.dump(dict(co_occur_count), open('data/co_occur.pkl', 'wb'))

    print('f(t,c): 単語tと文脈語cの共起回数: {0}'.format(len(co_occur_count)))
    print('f(t,∗): 単語tの出現回数: {0}'.format(len(word_count)))
    print('f(∗,c): 文脈語cの出現回数: {0}'.format(len(cont_count)))
    print('N: 単語と文脈語のペアの総出現回数: {0}'.format(N))


if __name__ == '__main__':
    main()
