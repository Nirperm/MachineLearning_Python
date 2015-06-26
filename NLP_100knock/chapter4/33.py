"""
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
"""


from section_30 import make_mecab_data


mecab_dict_list = make_mecab_data()
conjugational_plagal_verb_list = []
for mecab_dict in mecab_dict_list:
    if mecab_dict['pos1'] == 'サ変接続':
        conjugational_plagal_verb_list.append(mecab_dict['base'])

print(list(set(conjugational_plagal_verb_list)))
