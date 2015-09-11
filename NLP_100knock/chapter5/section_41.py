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

from section_40 import Morph
from collections import defaultdict


class Chunk:
    symbol_list = ['「', '」', '（', '）', '、', '。']

    def __init__(self,  dst, num):
        self.dst = dst
        self.srcs = list()
        self.morphs = []
        self.num = num

    def append_morph(self, mecab_result):
        self.morphs.append(Morph(mecab_result))

    def __str__(self):
        string = ''
        for morph in self.morphs:
            string += morph.surface
        return string + '\t' + self.dst + '\t' + ','.join(self.srcs)

    def get_phrase(self):
        phrase = ''
        for morph in self.morphs:
            if morph.surface in self.symbol_list:
                continue
            phrase += morph.surface
        return phrase

    def check_phrase_pos(self, pos):
        for morph in self.morphs:
            if morph.pos == pos:
                return True
        return False

    def get_pos_word(self, pos):
        phrase = ''
        for morph in self.morphs:
            if morph.pos == pos:
                if pos == '助詞':
                    phrase += morph.surface + ' '
                elif pos == '動詞':
                    phrase += morph.base
                    break
        return phrase

    def check_phrase_pos1(self, pos1):
        for morph in self.morphs:
            if morph.pos1 == pos1:
                return True
        return False

    def check_phrase_word(self, word):
        for morph in self.morphs:
            if morph.surface == word:
                return True
        return False

    def phrase_replace(self, pos, re_word):
        phrase = ''
        for morph in self.morphs:
            if morph.surface in self.symbol_list:
                continue
            if morph.pos == pos:
                if phrase not in re_word:
                    phrase += re_word
            else:
                phrase += morph.surface
        return phrase

    def root_word(self, sentence_chunk_list, dst):
        word_dst = dst
        while word_dst != '-1':
            word_dst = sentence_chunk_list[word_dst].dst
        return sentence_chunk_list[word_dst].get_phrase()


def make_text_chunk():
    text_chunk_list = []
    sentence_chunk_list = []
    srcs_dict = defaultdict(list)
    count = 0
    for line in open('./data/neko.txt.cabocha', 'r'):
        if line[:3] == 'EOS':
            count = 0
            for num in range(len(sentence_chunk_list)):
                sentence_chunk_list[num].srcs = srcs_dict[str(num)]
            text_chunk_list.append(sentence_chunk_list)

            sentence_chunk_list = []
            srcs_dict = defaultdict(list)

        elif line[:2] == '* ':
            chunk_info = line.strip().split(' ')
            chunk_info[2] = chunk_info[2].rstrip('D')
            phrase_chunk = Chunk(chunk_info[2], count)
            srcs_dict[chunk_info[2]].append(chunk_info[1])
            sentence_chunk_list.append(phrase_chunk)
            count += 1
        else:
            phrase_chunk.morphs.append(Morph(line))
    return text_chunk_list


if __name__ == '__main__':
    text_chunk_list = make_text_chunk()
    count = 0
    for sentence_chunk_list in text_chunk_list:
        count += 1
        for chunk in sentence_chunk_list:
            if count == 8:
                print(chunk)
