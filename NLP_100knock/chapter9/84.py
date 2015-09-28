"""
84. 単語文脈行列の作成
83の出力を利用し，単語文脈行列Xを作成せよ．
ただし，行列Xの各要素Xtcは次のように定義する．

f(t,c)≥10ならば，Xtc=PPMI(t,c)=max{logN×f(t,c)f(t,∗)×f(∗,c),0}
f(t,c)<10ならば，Xtc=0
ここで，PPMI(t,c)はPositive Pointwise Mutual Information（正の相互情報量）と呼ばれる統計量である．
なお，行列Xの行数・列数は数百万オーダとなり，行列のすべての要素を主記憶上に載せることは無理なので注意すること．
幸い，行列Xのほとんどの要素は0になるので，非0の要素だけを書き出せばよい．

"""

import math
import pickle
import scipy.sparse as sp
from collections import defaultdict

uni, con, co_occ, N = pickle.load(open('data/83_result.pkl', 'rb'))
Vt = 10000
Vc = 10000
X = sp.lil_matrix((Vt, Vc))
word2id = dict()

for i, tok in enumerate(uni.keys()):
    word2id[tok] = i
    if i == Vt:
        break
    for j, co in enumerate(con.keys()):
        if j == Vc:
            break
        if co_occ.get('%s %s' % (tok, co), 0) >= 10:
            X[i, j] = max(0, math.log((1.0 * N * co_occ['%s %s' % (tok, co)]) / (uni[tok] * con[co]), 2))
print(X)
pickle.dump(X, open('data/X.pkl', 'wb'))
pickle.dump(word2id, open('data/word2id.pkl', 'wb'))
