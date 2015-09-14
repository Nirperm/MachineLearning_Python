"""
48. 名詞から根へのパスの抽出
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ．
ただし，構文木上のパスは以下の仕様を満たすものとする．

各文節は（表層形の）形態素列で表現する
パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，
次のような出力が得られるはずである．

吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
"""

import sys
from section_41 import make_text_chunk


# FIXME: bugy

def extract_noun_to_root(sentence_chunk_list, noun_phrase, dst):
    while dst != '-1':

        sys.stdout.write('-> ' + sentence_chunk_list[int(dst)].get_phrase() + '\t')
        dst = sentence_chunk_list[int(dst)].dst


def get_pass(text_chunk_list):
    noun = '名詞'
    for sentence_chunk_list in text_chunk_list:
        for chunk in sentence_chunk_list:
            if chunk.check_phrase_pos(noun) and chunk.dst != '-1':
                noun_phrase = chunk.get_phrase()
                extract_noun_to_root(sentence_chunk_list, noun_phrase, chunk.dst)
        print('\n')


if __name__ == '__main__':
    text_chunk_list = make_text_chunk()
    get_pass(text_chunk_list)
