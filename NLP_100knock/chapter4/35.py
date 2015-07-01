"""
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

"""


from section_30 import make_mecab_data
import re

# 最大、9-ngram
non_list = []
mecab_dict_list = make_mecab_data()

for i, mecab_dict in enumerate(mecab_dict_list):
    try:
        # TODO 連続していない名詞もとれている
        if mecab_dict['pos'] == '名詞' and mecab_dict_list[i]['pos'] == '名詞':
            non_list.append(mecab_dict['surface'])
        else:
            non_list.append('@')

    except IndexError:
        pass

str_non = '@'.join(non_list)
result = re.sub(r'@{2,}', ',', str_non)
replace_list = result.replace('@', '').split(',')
non_juncture_list = []
for word in replace_list:
    if len(word) >= 2:
        non_juncture_list.append(word)

print(non_juncture_list)
