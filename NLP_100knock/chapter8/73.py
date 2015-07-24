"""
73. 学習
72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．
"""

from sklearn import linear_model

# FIXME: prepare featuure data
logreg = linear_model.LogisticRegression()
# logreg.fit(X, Y)


if __name__ == '__main__':
    with open('data/sentiment.txt', encoding='utf-8') as f:
        content = f.read()
    content_list = content.replace('\t', ' ') \
                          .replace('</>', '') \
                          .replace('[', '') \
                          .replace(']', '') \
                          .strip().split()
