"""
72. 素性抽出
極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
素性としては，レビューからストップワードを除去し，
各単語をステミング処理したものが最低限のベースラインとなるであろう．
"""

import gensim
from constant import STOPWORDS
from nltk.stem import WordNetLemmatizer


if __name__ == '__main__':
    with open('data/sentiment.txt', encoding='utf-8') as f:
        lines = f.readlines()

    lemmatiser = WordNetLemmatizer()
    stems = [[lemmatiser.lemmatize(word, pos='v') for word in line.split() if word not in STOPWORDS] for line in lines]  # 10661 size

    label_list = [1 if line[:2] == '+1' else 0 for line in lines]
    # TODO: とりあえず行分のラベルはできたが、単語数には合っていない

    """ 辞書オブジェクトの作成 """
    dictionary = gensim.corpora.Dictionary(stems)
    dictionary.save('/tmp/deerwester.dict')

    """ 辞書オブジェクトの語彙で低頻度と高頻度のワードは除く """
    dictionary.filter_extremes(no_below=3, no_above=0.6)

    corpus = [dictionary.doc2bow(stem) for stem in stems]
    gensim.corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus)
    dictionary = gensim.corpora.Dictionary.load('/tmp/deerwester.dict')
    corpus = gensim.corpora.MmCorpus('/tmp/deerwester.mm')

    tfidf = gensim.models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    lsi = gensim.models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)

    corpus_lsi = lsi[corpus_tfidf]
    for doc in tfidf[corpus]:
        print(doc)
