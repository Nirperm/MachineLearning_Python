"""
59. S式の解析
Stanford Core NLPの句構造解析の結果（S式）を読み込み，
文中のすべての名詞句（NP）を表示せよ．
入れ子になっている名詞句もすべて表示すること．
"""

from collections import Counter


def extract_np(xml_name):
    parse_tag = '<parse>'
    for line in open(xml_name):
        if parse_tag in line:
            word_list = line.split(' ')
            for begin in range(len(word_list)):
                if 'NP' in word_list[begin]:
                    count = 1
                    for num in range(begin + 1, len(word_list)):
                        word = word_list[num]
                        if '(' in word:
                            count += 1
                        elif ')' in word:
                            count -= word.count(')')
                            print(word.replace(')', ''))
                        if count < 1:
                            break
                    print('')
            print('')


if __name__ == '__main__':
    file_name = 'data/nlp.xml'
    extract_np(file_name)
