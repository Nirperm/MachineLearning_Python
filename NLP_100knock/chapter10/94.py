"""
94. WordSimilarity-353での類似度計算
The WordSimilarity-353 Test Collectionの評価データを入力とし，
1列目と2列目の単語の類似度を計算し，各行の末尾に類似度の値を追加するプログラムを作成せよ．
このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
"""

from gensim.models import word2vec

# TODO: apply 85 PCA vector


def calc_sim(data, model):
    f = open('data/word_similarity-353.txt', 'w')
    for line in data[1:]:
        line = line.strip()
        word1, word2 = line.split(',')[:2]
        try:
            sim = model.similarity(word1, word2)
            f.write(line + '\t' + str(sim) + '\n')
        except:
            pass
    f.close()


if __name__ == '__main__':
    model = word2vec.Word2Vec.load_word2vec_format('data/fb_post.bin', binary=True)
    data = open('data/wordsim353/combined.csv', 'r').readlines()
    calc_sim(data, model)
