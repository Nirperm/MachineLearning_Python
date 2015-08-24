"""
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import MeCab


def load_txt(filepath):
    """ テキスト読込を行う """

    with open(filepath, 'r') as f:
        txt = f.read()
    return txt


def analyze(txt):
    """ 形態素解析を行う """
    mt = MeCab.Tagger('-Ochasen')
    return mt.parse(txt)


def dictnize(txt):
    """ chasen形式の文字列を辞書に変換する """

    buf = txt.split("\n")
    dics = filter(lambda x: x, map(lambda x: texts2dic(x.split()), buf))
    return dics


def texts2dic(txt_list):
    if len(txt_list) < 4:
        return None

    morph_dic = {}
    morph_dic['surface'] = txt_list[0]
    morph_dic['pronunce'] = txt_list[1]

    morph_dic['base'] = txt_list[2]
    poses = txt_list[3].split("-")
    morph_dic['pos'] = poses[0]
    if len(poses) > 1:
        morph_dic['pos1'] = poses[1]
    return morph_dic


if __name__ == '__main__':
    txt = load_txt('./data/neko.txt')
    morph = analyze(txt)
    morph_dics = dictnize(morph)
    for x in morph_dics:
        print(x)
