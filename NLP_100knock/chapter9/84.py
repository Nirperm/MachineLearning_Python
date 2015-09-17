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
import numpy
import pickle
from collections import defaultdict

ppml_dict = defaultdict(lambda: defaultdict(float))
cont_dict = pickle.load(open('data/cont.pkl', 'rb'))
word_dict = pickle.load(open('data/word.pkl', 'rb'))
co_occur_dict = pickle.load(open('data/co_occur.pkl', 'rb'))

print('start store ppmi')
voc_set = set()
count = 68104854  #=> 142425660 N: 単語と文脈語のペアの総出現回数: 68104854
for pair, freq in co_occur_dict.items():
    if freq > 9:
        word, cont = pair.split('\t')
        numer = count * freq
        denom = word_dict[word] * cont_dict[cont]
        if numer > denom:
            voc_set.update(cont)
            ppml_dict[word][cont] = math.log(numer / float(denom))
voc_set.update(word_dict.keys())

print('start convert to matrix')
vocablary = sorted(ppml_dict.keys())
all_voc = sorted(list(voc_set))
term_document_matrix = numpy.zeros((len(all_voc), len(vocablary)))

"""
print('make_zeros_matrix')
x_count = 0
for x_voc in vocablary:
    temp_matrix = term_document_matrix[x_count]
    y_count = 0
    x_count += 1
    for y_voc in all_voc:
        if x_voc in ppml_dict and y_voc in ppml_dict[x_voc]:
            temp_matrix[y_count] = (ppml_dict[x_voc][y_voc])
            y_count += 1
"""
print('write csv')
numpy.savetxt('data/matrix.csv', term_document_matrix, delimiter=',')
