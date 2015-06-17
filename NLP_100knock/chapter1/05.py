"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""


def n_gram(sequence, n):
    return [sequence[k: k + n] for k in range(len(sequence) - n + 1)]

string = 'I am an NLPer'
print(n_gram(string, 2))
print(','.join(n_gram(string, 2)))
