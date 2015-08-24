"""
31. 動詞
動詞の表層形をすべて抽出せよ．
"""


from section_30 import load_txt
from section_30 import analyze
from section_30 import dictnize


def extract_verb(morph_dics):
    """ 動詞を抽出する """
    return filter(lambda x: x['pos'] == '動詞', morph_dics)


if __name__ == '__main__':
    txt = load_txt('./data/neko.txt')
    morph = analyze(txt)
    verb = extract_verb(dictnize(morph))
    for v in verb:
        print(v)
