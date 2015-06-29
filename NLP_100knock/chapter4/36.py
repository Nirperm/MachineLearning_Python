"""
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，
出現頻度の高い順に並べよ．
"""

from section_30 import make_mecab_data

mecab_dict_list = make_mecab_data()
word_count_dict = {}

for i, mecab_dict in enumerate(mecab_dict_list):
    if mecab_dict['surface'] not in word_count_dict:
        word_count_dict[mecab_dict['surface']] = 0
    word_count_dict[mecab_dict['surface']] += 1

for word, count in sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True):
    print(word, count)
