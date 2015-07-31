"""
72. 素性抽出
極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
素性としては，レビューからストップワードを除去し，
各単語をステミング処理したものが最低限のベースラインとなるであろう．
"""

import numpy as np
import gensim
from collections import namedtuple
from constant import STOPWORDS
from nltk.stem import WordNetLemmatizer


def load_sentiment():
    with open('data/sentiment.txt', encoding='utf-8') as f:
        lines = f.readlines()

    lemmatiser = WordNetLemmatizer()
    stems = [[lemmatiser.lemmatize(word, pos='v') for word in line.split() if word not in STOPWORDS] for line in lines]  # 10661 size

    label_list = [1 if line[:2] == '+1' else 0 for line in lines]
    target = np.asarray(label_list)

    dictionary = gensim.corpora.Dictionary(stems)

    dictionary.save('/tmp/deerwester.dict')

    """ 辞書オブジェクトの語彙で低頻度と高頻度のワードは除く """
    dictionary.filter_extremes(no_below=3, no_above=0.6)

    corpus = [dictionary.doc2bow(stem) for stem in stems]

    gensim.corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus)

    # tfidf = gensim.models.TfidfModel(corpus) FIXME: is this necessary?
    numpy_matrix = gensim.matutils.corpus2dense(corpus, num_terms=len(corpus))

    Sentiment = namedtuple("Sentiment", "data target")
    sentiment = Sentiment(numpy_matrix, label_list)
    return sentiment


if __name__ == '__main__':
    sentiment = load_sentiment()
    print(sentiment)
