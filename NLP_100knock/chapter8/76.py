"""
76. ラベル付け
学習データに対してロジスティック回帰モデルを適用し，
正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．
"""

import math
from constant import STOPWORDS
from nltk.stem import WordNetLemmatizer


def read_model(d):
    for line in open('data/73_model.txt'):
        if line.startswith('@'):
            continue
        spl = line.strip().split()
        d[spl[1]] = float(spl[0])


def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))


def extract_features(text):
    lemmatiser = WordNetLemmatizer()
    return [lemmatiser.lemmatize(tok, pos='v') for tok in text if not tok in STOPWORDS]


def probability(feat):
    return sigmoid(sum(model.get(f, 0) for f in feat))


def predict(prob, thresh):
    return '-1' if prob < thresh else '+1'

model = dict()
read_model(model)
for line in open('data/sentiment.txt'):
    spl = line.strip().split()
    label = spl[0]
    feat = extract_features(spl[1:])
    prob = probability(feat)
    print('%s\t%s\t%f' % (label, predict(prob, 0.5), prob))
