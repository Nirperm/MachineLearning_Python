"""
49. 名詞間の係り受けパスの抽出
文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．

問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を"->"で連結して表現する
文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
また，係り受けパスの形状は，以下の2通りが考えられる．

文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合: 文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を"|"で連結して表示
例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

Xは | Yで -> 始めて -> 人間という -> ものを | 見た
Xは | Yという -> ものを | 見た
Xは | Yを | 見た
Xで -> 始めて -> Y
Xで -> 始めて -> 人間という -> Y
Xという -> Y

"""

import sys
from section_41 import make_text_chunk


def root_word(sentence_chunk_list, dst):
    word_dst = dst
    prev_dst = int(dst)

    while word_dst != '-1':
        word_dst = int(word_dst)
        prev_dst = word_dst
        word_dst = sentence_chunk_list[word_dst].dst
    return sentence_chunk_list[prev_dst].get_phrase()


def extract_noun_to_root(sentence_chunk_list, noun_phrase, dst):
    # next_dst = sentence_chunk_list[int(dst)].dst
    sys.stdout.write(noun_phrase)

    while 1:
        if sentence_chunk_list[int(dst)].dst == '-1':
            break
        sys.stdout.write('-> ' + sentence_chunk_list[int(dst)].get_phrase(),)
        dst = sentence_chunk_list[int(dst)].dst
        # next_dst = sentence_chunk_list[int(dst)].dst
        # sys.stdout.write(dst + next_dst)


def make_phrase_list(sentence_chunk_list, noun_phrase, dst):
    phrase_list = list()
    phrase_list.append(noun_phrase)
    while sentence_chunk_list[int(dst)].dst != '-1':
        phrase_list.append(sentence_chunk_list[int(dst)].get_phrase())
        dst = sentence_chunk_list[int(dst)].dst
    return phrase_list


def check_same_phrase(phrase_list1, phrase_list2):
    for phrase in phrase_list1:
        if phrase in phrase_list2:
            return True, phrase

    return False, 'NULL'


def make_minimum_pass(sentence_chunk_list, noun_num_list):
    # particle = '助詞'
    noun = '名詞'
    match_flag = False
    count = 0
    sub_noun_num_list = list(noun_num_list)
    for phrase_num in noun_num_list:
        count += 1
        sub_noun_num_list.remove(phrase_num)
        chunk = sentence_chunk_list[phrase_num]
        first_word = chunk.phrase_replace(noun, 'X')
        top_phrase_list = make_phrase_list(sentence_chunk_list, chunk.get_phrase(), chunk.dst)
        for other_num in sub_noun_num_list:
            next_chunk = sentence_chunk_list[other_num]
            next_phrase_list = make_phrase_list(sentence_chunk_list, next_chunk.get_phrase(), next_chunk.dst)
            match_flag, match_num = check_same_phrase(top_phrase_list, next_phrase_list[:-1])
            sys.stdout.write(first_word)
            if match_flag:
                sys.stdout.write(' -> ' + ' -> '.join(next_phrase_list[:-1]) + ' -> Y')
            else:
                print(' | ',)
                extract_noun_to_root(sentence_chunk_list, next_chunk.phrase_replace(noun, 'Y'), next_chunk.dst)
                if not next_chunk.get_phrase() == root_word(sentence_chunk_list, chunk.dst):
                    sys.stdout.write(' | ' + root_word(sentence_chunk_list, chunk.dst))


def make_noun_num_list(sentence_chunk_list):
    noun_num_list = list()
    noun = '名詞'
    for chunk in sentence_chunk_list:
        if chunk.check_phrase_pos(noun):
            noun_num_list.append(chunk.num)
    return noun_num_list


def get_trace_pass(text_chunk_list):
    for sentence_chunk_list in text_chunk_list:
        # check_print = False

        noun_num_list = make_noun_num_list(sentence_chunk_list)
        if noun_num_list != []:
            make_minimum_pass(sentence_chunk_list, noun_num_list)


if __name__ == '__main__':
    text_chunk_list = make_text_chunk()
    get_trace_pass(text_chunk_list)
