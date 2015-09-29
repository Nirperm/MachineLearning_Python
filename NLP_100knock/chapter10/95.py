"""
95. WordSimilarity-353での評価
94で作ったデータを用い，各モデルが出力する類似度のランキングと，
人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．
"""


rank_human = dict()
rank_word2 = dict()

l = list()
for line in open('data/word_similarity-353.txt'):
    spl = line.strip().replace('\t', ',').split(',')
    l.append((','.join(spl[:2]), float(spl[2]), float(spl[3])))

for rank, (key, _ , _) in enumerate(sorted(l, key=lambda x: -x[1])):
    rank = rank + 1
    rank_human[key] = rank

for rank, (key, _ ,_) in enumerate(sorted(l, key=lambda x: -x[2])):
    rank = rank + 1
    rank_word2[key] = rank

N = len(rank_human.keys())
rho = 1 - (6.0 * sum((rank_human[k] - rank_word2[k]) ** 2 for k in rank_human.keys())) / (N ** 3 - N)
print(rho)
