"""
01. 「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"""

string = '「パタトクカシーー」'
word_list = []

for i in range(len(string)):
    if i > 7:
        break

    if i % 2:
        word_list.append(string[i])

print(' '.join(word_list))
