"""
72. 素性抽出
極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
素性としては，レビューからストップワードを除去し，
各単語をステミング処理したものが最低限のベースラインとなるであろう．
"""

from collections import namedtuple
from constant import STOPWORDS
from nltk.stem import WordNetLemmatizer


def load_sentiment():
    with open('data/sentiment.txt', encoding='utf-8') as f:
        lines = f.readlines()
    return lines


def stem(lines):
    lemmatiser = WordNetLemmatizer()
    stems = [[lemmatiser.lemmatize(word, pos='v') for word in line.split() if word not in STOPWORDS] for line in lines]  # 10661 size
    return stems


def create_feture(stems, lines):
    target_labels = [1 if line[:2] == '+1' else 0 for line in lines]
    Sentiment = namedtuple("Sentiment", ["data", "target"])
    feature = Sentiment(stems, target_labels)
    return feature


if __name__ == '__main__':
    lines = load_sentiment()
    stems = stem(lines)
    feature = create_feture(stems, lines)
    print(feature.data, feature.target)
