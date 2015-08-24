"""
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

from section_30 import load_txt
from section_30 import analyze
from section_30 import dictnize


def extract_noun_seqs(morph_dics):
    """ 連続している名詞を抽出する """

    dics = list(morph_dics)

    seqs = []
    seq = []
    for i in range(len(dics)):
        if dics[i]['pos'] == '名詞':
            seq.append(dics[i]['surface'])
        else:
            if seq:
                seqs.append(seq)

            seq = []

    words = filter(lambda x: len(x) > 1, seqs)
    return map(lambda x: ''.join(x), words)


if __name__ == '__main__':
    txt = load_txt('./data/neko.txt')
    morph = analyze(txt)
    n_seq = extract_noun_seqs(dictnize(morph))
    for x in n_seq:
        print(x)
