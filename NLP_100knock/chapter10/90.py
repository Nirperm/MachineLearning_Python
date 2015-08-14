"""
90. word2vecによる学習
81で作成したコーパスに対してword2vecを適用し，単語ベクトルを学習せよ．
さらに，学習した単語ベクトルの形式を変換し，86-89のプログラムを動かせ．
"""

# FIXME: Too heavy

import gensim


def vectolize():
    with open('data/81_result.txt', encoding='utf') as f:
        lines = f.readlines()

    words = [[word for word in line.split()] for line in lines]
    dictionary = gensim.corpora.Dictionary(words)
    dictionary.save('/tmp/section90.dict')

    """ 辞書オブジェクトの語彙で低頻度と高頻度のワードは除く """
    dictionary.filter_extremes(no_below=3, no_above=0.6)

    corpus = [dictionary.doc2bow(word) for word in words]

    gensim.corpora.MmCorpus.serialize('/tmp/section72.mm', corpus)

    numpy_matrix = gensim.matutils.corpus2dense(corpus, num_terms=len(corpus))
    print(numpy_matrix)

if __name__ == '__main__':
    vectolize()
