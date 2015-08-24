"""
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
"""

from section_30 import load_txt
from section_30 import analyze
from section_30 import dictnize


def extract_sahen(morph_dics):
    """ サ変接続を抽出する """
    ns = filter(lambda x: x['pos'] == '名詞', morph_dics)
    ns_pos1 = filter(lambda x: 'pos1' in x, ns)
    return filter(lambda x: x['pos1'] == 'サ変接続', ns_pos1)


if __name__ == '__main__':
    txt = load_txt('./data/neko.txt')
    morph = analyze(txt)
    dictnize(morph)
    sahens = extract_sahen(dictnize(morph))
    for x in sahens:
        print(x)
