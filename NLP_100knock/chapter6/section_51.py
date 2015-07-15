"""
51. 単語の切り出し
空白を単語の区切りとみなし，50の出力を入力として受け取り，
1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．
"""

from section_50 import divide_content


def divide_word(sentence_list):
    content = ' '.join(sentence_list)
    content_list = content.split(' ')
    word_list = []
    for word in content_list:
        if word == '-':
            word = ''
        word_list.append(word.replace(',', '').replace('"', '').replace('(', '').replace(')', '').replace('--', '').replace('\'', ''))
    return word_list


if __name__ == '__main__':
    sentence_list = divide_content()
    word_list = divide_word(sentence_list)
    for w in word_list:
        print(w)
