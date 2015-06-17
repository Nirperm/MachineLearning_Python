"""
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文
（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
"""

import random

string = 'I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'

split_list = string.split()
typoglycemia_list = []

for word in split_list:
    if len(word) >= 4:
        begging_word = word[0]
        ending_word = word[-1]
        rand_word = random.sample(word, len(word))
        rand_word[:1] = begging_word  # HACK: I don't know why string#replace doesn't work well
        rand_word[-1:] = ending_word
        typoglycemia = ''.join(rand_word)
        typoglycemia_list.append(typoglycemia)
    else:
        typoglycemia_list.append(word)

typoglycemia_line = ','.join(typoglycemia_list).replace(',', ' ')

print('Original str : ', string, '\n')
print('Typoglycemia : ', typoglycemia_line)
