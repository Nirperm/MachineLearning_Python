import pickle
import scipy
import sklearn.decomposition

dim = 300
X = pickle.load(open('data/X.pkl', 'rb'))
pca = sklearn.decomposition.PCA(dim)
Xpca = pca.fit_transform(X.toarray())
print(Xpca)
pickle.dump(Xpca, open('data/Xpca.pkl', 'wb'))
