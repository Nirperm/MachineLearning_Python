"""
71. ストップワード
英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，
それ以外は偽を返す関数を実装せよ．
さらに，その関数に対するテストを記述せよ．
"""


from constant import stopwords


def stop_word(word):

    if word in stopwords:
        print('True' + '\t' + word)
    else:
        print('False' + '\t' + word)


if __name__ == '__main__':
    with open('data/sentiment.txt', encoding='utf-8') as f:
        for line in f:
            line_list = line.replace('\t', ' ').strip().split(' ')
            for word in line_list:
                stop_word(word)
