"""
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
"""

from section_41 import make_text_chunk


def pair_noun_dependency_verb(text_chunk_list):
    noun = '名詞'
    verb = '動詞'
    for sentence_chunk_list in text_chunk_list:
        check_print = False
        for chunk in sentence_chunk_list:
            if chunk.check_phrase_pos(noun) and chunk.dst != '-1' and sentence_chunk_list[int(chunk.dst)].check_phrase_pos(verb):
                print(chunk.get_phrase(), '\t', sentence_chunk_list[int(chunk.dst)].get_phrase())
                check_print = True

if __name__ == '__main__':
    text_chunk_list = make_text_chunk()
    pair_noun_dependency_verb(text_chunk_list)
