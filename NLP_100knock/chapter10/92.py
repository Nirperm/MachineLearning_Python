import numpy
from gensim.models import word2vec




def get_vec(word):
    return word2_vec[word]

"""
def vec_cos(x, y):
    return numpy.dot(x, y) / (numpy.linalg.norm(x) * numpy.linalg.norm(y))




def max_similar(a, b, c):
    vector = get_vec(b) - get_vec(a) + get_vec(c)
    gyo, retu = matrix_data.shape
    cos_list = list()
    for num in range(gyo):
        cos_list.append(vec_cos(vector, matrix_data[num]))
    descend_list = sorted(cos_list, reverse=True)
    for score in descend_list[0:1]:
        print(voc[cos_list.index(score)], score)


def max_similar_alpha(a, b, c, d):
    vector = (get_vec(b) - get_vec(a)) * 2 + get_vec(c)
    print(vector)
    gyo, retu = matrix_data.shape
    cos_list = list()
    for num in range(gyo):
        cos_list.append(vec_cos(vector, matrix_data[num]))
    descend_list = sorted(cos_list, reverse=True)
    for score in descend_list[0:1]:
        print(voc[cos_list.index(score)], score)
    print(vec_cos(vector, get_vec(d)))
"""

def culc_vec(fname):
    for line in open(fname):
        if not line.startswith(': family'):
            a, b, c, d = line.split(' ')
            print(line.strip(),)
            print(word2_vec[a])
            """
            try:
                max_similar_alpha(a, b, c, d.strip())
            except KeyboardInterrupt:
                print('key interrupt')
                exit()
            except:
                print('None', 0)
            """


if __name__ == '__main__':
    # matrix_data = numpy.genfromtxt('vector.csv', delimiter = ',')
    # matrix_data[numpy.isnan(matrix_data)] = 0

    word2_vec = word2vec.Word2Vec.load_word2vec_format('data/fb_post.bin', binary=True)
    culc_vec("data/family.txt")
