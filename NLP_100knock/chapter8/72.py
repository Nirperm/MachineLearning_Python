"""
72. 素性抽出
極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
素性としては，レビューからストップワードを除去し，
各単語をステミング処理したものが最低限のベースラインとなるであろう．
"""

import re
from constant import STOPWORDS
from gensim import corpora
# from gensim import models
from nltk.stem import WordNetLemmatizer


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
            yield lemmatiser.lemmatize(word, pos='v').rstrip().split()


class MyCorpus():
    def __init__(self, dictionary, sentence_list):
        self.dic = dictionary
        self.sentence = sentence_list

    def __iter__(self):
        for word in self.sentence:
            yield self.dic.doc2bow(word.split())

if __name__ == '__main__':
    with open('data/sentiment.txt', encoding='utf-8') as f:
        content = f.read()
    content_list = content.replace('\t', ' ') \
                          .replace('</>', '') \
                          .replace('[', '') \
                          .replace(']', '') \
                          .strip().split()

    sentence_list = extract_sentence(content_list)
    stem = stemmer(sentence_list)
    """ 辞書オブジェクトの作成 """
    dictionary = corpora.Dictionary(stem)  # 17330 size
    print(dictionary.token2id)
    """ 辞書オブジェクトの語彙の削減 """
    """
    # dictionary.filter_extremes(no_below=100, no_above=0.2)  # 100回以上出現してかつ，出現頻度が2割を超えない単語の辞書 138 size
    corpus = MyCorpus(dictionary, sentence_list)
    lda = models.LdaModel(corpus, num_topics=60, id2word=dictionary)
    print(lda.show_topics(num_topics=5))
    """
