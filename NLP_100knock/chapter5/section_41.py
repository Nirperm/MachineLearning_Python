"""
41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは形態素（Morphオブジェクト）のリスト（morphs），
係り先文節インデックス番号（dst），
係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストのCaboChaの解析結果を読み込み，
１文をChunkオブジェクトのリストとして表現し，
8文目の文節の文字列と係り先を表示せよ．
第5章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

from section_40 import load_txt
from section_40 import analyze
from section_40 import spearate_element


def read_cabocha(result):
    dst_list = []
    srcs_list = []
    teos_list = []

    for line in result.split('\n'):
        ary = line.replace('\t', ',').split(',')
        if len(ary) is 1:
            teos_ary = ''.join(ary).split(' ')
            if len(teos_ary) > 1:
                dst_list.append(teos_ary[1])
                srcs_list.append(teos_ary[2])

                teos_list.append(dst_list)
                teos_list.append(srcs_list)

    return teos_list


class Chunk:

    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs


if __name__ == '__main__':
    txt = load_txt('./data/neko.txt')
    result = analyze(txt)
    cabocha_list = spearate_element(result)

    teos_list = read_cabocha(result)
    chunk = Chunk(cabocha_list[0], teos_list[0], teos_list[1])
    print(chunk.morphs[8], chunk.dst[8])
