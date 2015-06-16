"""
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""


def n_gram(sequence, n):
    return [sequence[k: k + n] for k in range(len(sequence) - n + 1)]

paradise = 'paraparaparadise'
paragraph = 'paragraph'

x = set(n_gram(paradise, 2))
y = set(n_gram(paragraph, 2))

print('Union = ' + ' ' + ','.join(list(x.union(y))))
print('Intersectio =n' + ' ' + ','.join(list(x.intersection(y))))
print('Difference =' + ' ' + ','.join(list(x.difference(y))))

print('Does x include "se"?' + ' ' + str('se' in x))
print('Does y include "se"?' + ' ' + str('se' in y))
