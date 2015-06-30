"""
40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．
このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""

surface_list = []
base_list = []
pos_list = []
pos1_list = []

with open('data/neko.txt.cabocha', encoding='utf-8') as f:
    for line in f:
        ary = line.replace('\t', ',').split(',')
        if len(ary) is 1:  # TODO: TEOSはとらなくて良いのか
            pass
        else:
            surface_list.append(ary[0])
            base_list.append(ary[-3])
            pos_list.append(ary[1])
            pos1_list.append(2)

"""
class Morph:

    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
"""
