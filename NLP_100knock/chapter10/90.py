"""
90. word2vecによる学習
81で作成したコーパスに対してword2vecを適用し，単語ベクトルを学習せよ．
さらに，学習した単語ベクトルの形式を変換し，86-89のプログラムを動かせ．
"""


from gensim.models import word2vec


def section_86(model):
    print('section_86')
    print(model['United_States'], '\n')


def section_87(model):
    print('section_87')
    print(model.n_similarity(['United_States'], ['U.S']), '\n')


def section_88(model):
    print('section_88')
    for w, s in model.most_similar(['England']):
        print(w, s)


def section_89(model):
    print('section_89')
    print(model['Spain'] + model['Athens'] - model['Madrid'], '\n')
    for w, s in model.most_similar(['Spain', 'Athens'], ['Madrid']):
        print(w, s)

if __name__ == '__main__':
    model = word2vec.Word2Vec.load_word2vec_format('data/fb_post.bin', binary=True)
    section_86(model)
    section_87(model)
    section_88(model)
    section_89(model)
