"""
83. 単語／文脈の頻度の計測
82の出力を利用し，以下の出現分布，および定数を求めよ．

f(t,c): 単語tと文脈語cの共起回数
f(t,∗): 単語tの出現回数
f(∗,c): 文脈語cの出現回数
N: 単語と文脈語のペアの総出現回数
"""

import pickle


def main():
    uni = dict()
    co_occ = dict()
    con = dict()

    for line in open('data/82_result.txt'):
        spl = line.strip().split('\t')
        uni[spl[0]] = uni.get(spl[0], 0) + 1
        for co in spl[1:]:
            key = "%s %s" % (spl[0], co)
            co_occ[key] = co_occ.get(key, 0) + 1
            con[co] = con.get(co, 0) + 1
    N = len(co_occ.keys())

    print('f(t,c): 単語tと文脈語cの共起回数: {0}'.format(len(co_occ)))
    print('f(t,∗): 単語tの出現回数: {0}'.format(len(uni)))
    print('f(∗,c): 文脈語cの出現回数: {0}'.format(len(con)))
    print('N: 単語と文脈語のペアの総出現回数: {0}'.format(N))

    pickle.dump([uni, con, co_occ, N], open('data/83_result.pkl', 'wb'))


if __name__ == '__main__':
    main()
