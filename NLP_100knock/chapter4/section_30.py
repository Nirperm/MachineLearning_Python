"""
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import copy


def make_mecab_data():

    mecab_dict_list = []
    d = {}

    with open('data/neko.txt.mecab', encoding='utf-8') as f:
        for line in f:
            ary = line.replace('\t', ',').replace('\n', '').split(',')
            if len(ary) is 1:
                d['surface'] = ary[0]
                d['base'] = None
                d['pos'] = None
                d['pos1'] = None
            else:
                d['surface'] = ary[0]
                d['base'] = ary[-3]
                d['pos'] = ary[1]
                d['pos1'] = ary[2]
            mecab_dict = copy.copy(d)
            mecab_dict_list.append(mecab_dict)
        return mecab_dict_list

if __name__ == '__main__':
    result = make_mecab_data()
    print(result)
