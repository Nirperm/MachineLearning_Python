"""
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""


from section_30 import make_mecab_data

non_juncture_list = []
mecab_dict_list = make_mecab_data()

for i, mecab_dict in enumerate(mecab_dict_list):
    if mecab_dict['pos'] == '名詞' and \
        (mecab_dict_list[i - 1]['pos'] == '名詞' or \
         mecab_dict_list[i + 1]['pos'] == '名詞'):
            non_juncture_list.append(mecab_dict_list[i - 1]['surface'] + \
                                     mecab_dict['base'] + \
                                     mecab_dict_list[i + 1]['surface'])

print(non_juncture_list)
