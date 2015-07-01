"""
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

"""


from section_30 import make_mecab_data

# 最大、9-ngram
non_juncture_list = []
mecab_dict_list = make_mecab_data()

for i, mecab_dict in enumerate(mecab_dict_list):
    try:
        if mecab_dict['pos'] == '名詞':
            if mecab_dict_list[i + 1]['pos'] == '名詞':
                non_juncture_list.append(mecab_dict['surface'] + mecab_dict_list[i + 1]['surface'])
    except IndexError:
        pass

print(non_juncture_list)
