"""
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
"""

from section_41 import make_text_chunk


def pair_modification_structure(text_chunk_list):
    for sentence_chunk_list in text_chunk_list:
        for chunk in sentence_chunk_list:
            if chunk.dst != '-1':
                print(chunk.get_phrase(), '\t', sentence_chunk_list[int(chunk.dst)].get_phrase(), '\n')

if __name__ == '__main__':
    text_chunk_list = make_text_chunk()
    pair_modification_structure(text_chunk_list)
