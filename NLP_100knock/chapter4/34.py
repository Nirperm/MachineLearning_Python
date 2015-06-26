"""
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""


from section_30 import make_mecab_data

mecab_dict_list = make_mecab_data()
nominal_list = []

for i, mecab_dict in enumerate(mecab_dict_list):
    if mecab_dict['pos1'] == '連体化' and \
        mecab_dict_list[i - 1]['pos'] == '名詞' and \
        mecab_dict_list[i + 1]['pos'] == '名詞':
                nominal_list.append(mecab_dict_list[i - 1]['surface'] + \
                                           mecab_dict['base'] + \
                                           mecab_dict_list[i + 1]['surface'])

print(list(set(nominal_list)))
