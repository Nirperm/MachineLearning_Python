"""
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import MeCab
# from collections import defaultdict

tagger = MeCab.Tagger("")
tagger.parse('')

# mecab_list = []
keyword_list = []
mecab_dict = {}
# with open('data/neko.txt', encoding='utf-8') as f:
#    for line in f:

f = open('data/neko.txt', 'r')
content = f.read()
# node = tagger.parseToNode(line)
node = tagger.parseToNode(content)
f.close()
while node:
    ary = node.feature.split(',')
    keyword_list.append(node.surface)
    keyword_list.append(ary[-3])
    keyword_list.append(ary[0])
    keyword_list.append(ary[1])
    node = node.next

chunks = [keyword_list[i:i + 4] for i in range(0, len(keyword_list), 4)]
print(chunks)


"""
使ってみる
dictionary = {}
dictionary.setdefault("list", []).append("list_item")
"""
