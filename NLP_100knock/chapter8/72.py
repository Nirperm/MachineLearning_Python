"""
72. 素性抽出
極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
素性としては，レビューからストップワードを除去し，
各単語をステミング処理したものが最低限のベースラインとなるであろう．
"""

import numpy as np
import re
import gensim
from constant import STOPWORDS
from gensim import corpora
# from gensim import models
from nltk.stem import WordNetLemmatizer


def vec2dense(vec, num_terms):
    ''' Convert from sparse gensim format to dense list of numbers '''
    return list(gensim.matutils.corpus2dense([vec], num_terms=num_terms).T[0])


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
            yield lemmatiser.lemmatize(word, pos='v').strip().split()


def extract_feature(dictionary, word_list):
    feature_list = []
    for word in word_list:
        sparse = dictionary.doc2bow(word.split())
        dense = vec2dense(sparse, num_terms=len(dictionary))
        feature_list.append(dense)
    return np.float32(feature_list)


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
    stems = stemmer(sentence_list)

    """ 辞書オブジェクトの作成 """
    dictionary = corpora.Dictionary(stems)  # 17330 size
    # unfiltered = dictionary.token2id.keys()

    """ 辞書オブジェクトの語彙で低頻度と高頻度のワードは除く """
    dictionary.filter_extremes(no_below=100, no_above=0.6)
    """
    filterd = dictionary.token2id.keys()
    filtered_out = set(unfiltered) - set(filterd)
    """

    word_list = []
    for stem_word in stemmer(sentence_list):
        word_list.append(stem_word[0])
    features = extract_feature(dictionary, word_list)

    # TODO: need label and gether features(as Collections#named_tuple)

    """
    corpus = MyCorpus(dictionary, sentence_list)
    lda = models.LdaModel(corpus, num_topics=60, id2word=dictionary)
    print(lda.show_topics())
    """
