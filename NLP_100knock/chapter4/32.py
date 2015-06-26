"""
32. 動詞の原形
動詞の原形をすべて抽出せよ．
"""

from section_30 import make_mecab_data


mecab_dict_list = make_mecab_data()
original_verb_list = []
for mecab_dict in mecab_dict_list:
    if mecab_dict['pos'] == '動詞':
        original_verb_list.append(mecab_dict['base'])

print(list(set(original_verb_list)))
