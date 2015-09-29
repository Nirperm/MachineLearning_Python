import pickle
import sys
sys.path.insert(0, '../chapter9')

from section_88 import similar_words
from gensim.models import word2vec


# FIXME: data/Xpca.txt is None,  something bugy

Xpca = pickle.load(open('../chapter9/data/Xpca.pkl', 'rb'))
word2id = pickle.load(open('../chapter9/data/word2id.pkl', 'rb'))
w2v_model = word2vec.Word2Vec.load_word2vec_format('data/fb_post.bin', binary=True)

f = open('data/w2v.txt', 'w')
for line in open('data/family.txt'):
    words = line.strip().split()
    if not w2v_model.__contains__(words[0]) or not w2v_model.__contains__(words[1]) or not w2v_model.__contains__(words[2]):
        continue
    f.write(line.strip() + ' ' + w2v_model.most_similar([words[1], words[2], words[0]], topn=1)[0][0] + '\n')
f.close()

f = open('data/Xpca.txt', 'w')
for line in open('data/family.txt'):
    words = line.strip().split()
    if not words[0] in word2id or not words[1] in word2id or not words[2] in word2id:
        break
    q = Xpca[word2id[words[1]]] - Xpca[word2id[word[0]]] + Xpca[word2id[words[2]]]
    f.write(lines.strip() + ' ' + similar_words(q, Xpca. word2id)[0][0] + '\n')
f.close()
