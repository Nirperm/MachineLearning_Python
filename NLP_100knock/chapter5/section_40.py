"""
40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．
このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""


import CaboCha


def load_txt(filepath):
    with open(filepath, 'r') as f:
        txt = f.read()
    return txt


def analyze(txt):
    """ Chabocha analyze """
    c = CaboCha.Parser('-f1')
    tree = c.parse(txt)
    return tree.toString(CaboCha.FORMAT_LATTICE)


def spearate_element(tree):
    cabocha_list = []
    surface_list = []
    base_list = []
    pos_list = []
    pos1_list = []
    morph_list = []

    for line in tree.split('\n'):
        ary = line.replace('\t', ',').split(',')
        morph_list.append(ary)
        cabocha_list.append(morph_list)
        if len(ary) is 1:
            pass
        else:
            surface_list.append(ary[0])
            base_list.append(ary[-3])
            pos_list.append(ary[1])
            pos1_list.append(ary[2])

            cabocha_list.append(surface_list)
            cabocha_list.append(base_list)
            cabocha_list.append(pos_list)
            cabocha_list.append(pos1_list)

    return cabocha_list


class Morph:

    def __init__(self, morphs, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
        self.morphs = morphs


if __name__ == '__main__':
    txt = load_txt('./data/neko.txt')
    result = analyze(txt)
    cabocha_list = spearate_element(result)
    morph = Morph(cabocha_list[0], cabocha_list[1], cabocha_list[2], cabocha_list[3], cabocha_list[4])
    print(morph.morphs[3])
