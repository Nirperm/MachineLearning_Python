

import pickle

Xpca = pickle.load(open('data/Xpca.pkl', 'rb'))
word2id = pickle.load(open('data/word2id.pkl', 'rb'))

i = word2id['United_States']
print(Xpca[i])
