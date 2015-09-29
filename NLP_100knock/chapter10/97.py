import pickle
import numpy as  np
from sklearn.cluster import KMeans

dic = pickle.load(open('data/countries.pkl', 'rb'))
features = [ np.array(v) for v in dic.values()]
km_model = KMeans(n_clusters=5).fit(features)
for label, name in sorted(zip(km_model.labels_, dic.keys()), key=lambda x: x[0]):
    print(label, name)
