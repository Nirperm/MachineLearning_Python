"""
72. 素性抽出
極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
素性としては，レビューからストップワードを除去し，
各単語をステミング処理したものが最低限のベースラインとなるであろう．
"""

import re
from constant import STOPWORDS
from nltk.stem import WordNetLemmatizer

# TODO: create data index colum neg/pos word

def extract_sentence(content_list):
    sentence_list = []
    for word in content_list:
        if word not in STOPWORDS:
            sentence_list.append(word)
    return sentence_list


def stemmer(sentence_list):
    lemmatiser = WordNetLemmatizer()

    for word in sentence_list:
        word = re.sub(r"^'", '', word)
        word = re.sub(r"^-", '', word)
        word = re.sub(r"'$", '', word)
        word = re.sub(r"^\d*-\S+", '', word)
        word = re.sub(r"^\d+\/\d", '', word)
        word = re.sub(r"^\d+", '', word)
        if len(word) is not 0:
            print(lemmatiser.lemmatize(word, pos='v'))


if __name__ == '__main__':
    with open('data/sentiment.txt', encoding='utf-8') as f:
        content = f.read()
    content_list = content.replace('\t', ' ') \
                          .replace('</>', '') \
                          .replace('[', '') \
                          .replace(']', '') \
                          .strip().split()

    sentence_list = extract_sentence(content_list)
    stemmer(sentence_list)
