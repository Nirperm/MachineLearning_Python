

import pickle
import numpy
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
