"""
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

from section_30 import load_txt
from section_30 import analyze
from section_30 import dictnize


def abstract_no(morph_dics):
    """ 'の'が出現するインデックスを求めてその両脇が名詞の場合名詞句を返す """

    dics = list(morph_dics)
    nos = []

    for i, x in enumerate(dics):
        if x['surface'] == 'の':
            if contain_no(i, dics):
                nos.append(dics[i - 1]['surface'] + dics[i]['surface'] + dics[i+ 1]['surface'])
    return nos


def contain_no(i, morph_dics):
    """ 名詞と名詞の間かどうか判定 """

    if morph_dics[i - 1]['pos'] == '名詞' and morph_dics[i + 1]['pos'] == '名詞':
        return True
    else:
        return False


if __name__ == '__main__':
    txt = load_txt('./data/neko.txt')
    morph = analyze(txt)
    nos = abstract_no(dictnize(morph))
    for x in nos:
        print(x)
