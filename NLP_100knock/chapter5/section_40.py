"""
40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．
このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，
各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""


class Morph:
    def __init__(self, mecab_result):
        result = mecab_result.replace('\t', ',').split(',')
        self.surface = result[0]
        self.base = result[7]
        self.pos = result[1]
        self.pos1 = result[2]

    def __str__(self):
        result = 'surface:%s\t base:%s\t pos:%s\tpos1:%s\t' % (self.surface, self.base, self.pos, self.pos1)
        return result


def make_morphs():
    sentence_morph_list = []
    text_morph_list = []

    for line in open('./data/neko.txt.cabocha', 'r'):
        if line[0] == '*':
            continue
        elif line[0:3] == 'EOS':
            text_morph_list.append(sentence_morph_list)
            sentence_morph_list = []
        else:
            sentence_morph_list.append(Morph(line))
    return text_morph_list


if __name__ == '__main__':
    text_morph_list = make_morphs()
    for morph in text_morph_list[2]:
        print(morph)
