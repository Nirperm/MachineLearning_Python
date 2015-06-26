"""
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""


from section_30 import make_mecab_data

non_juncture_list = []
mecab_dict_list = make_mecab_data()
