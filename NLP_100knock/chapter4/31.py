"""
31. 動詞
動詞の表層形をすべて抽出せよ．
"""


from section_30 import make_mecab_data

mecab_dict_list = make_mecab_data()
verb_list = []
for mecab_dict in mecab_dict_list:
    if mecab_dict['pos'] == '動詞':
        verb_list.append(mecab_dict['surface'])

print(list(set(verb_list)))
