"""
32. 動詞の原形
動詞の原形をすべて抽出せよ．
"""

from section_30 import load_txt
from section_30 import analyze
from section_30 import dictnize
from section_31 import extract_verb


def extract_base(verb):
    """ 原型を抽出する """
    return map(lambda x: x['base'], verb)


if __name__ == '__main__':
    txt = load_txt('./data/neko.txt')
    morph = analyze(txt)
    verb = extract_verb(dictnize(morph))
    vbases = extract_base(verb)
    for x in vbases:
        print(x)
