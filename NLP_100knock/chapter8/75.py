"""
75. 素性の重み
73で学習したロジスティック回帰モデルの中で，
重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．
"""

import gensim
import os
import re
import subprocess
from section_72 import load_txt
from section_72 import stem
from section_72 import create_feature
from section_73 import modelize


def create_dict(stems):
    dictionary = gensim.corpora.Dictionary(stems)
    dictionary.save('/tmp/chapter8.dict')
    return dictionary


def create_corpus(dictionary, stems):
    corpus = [dictionary.doc2bow(stem) for stem in stems]
    gensim.corpora.MmCorpus.serialize('/tmp/chapter8.mm', corpus)


def create_scale(corpus, feature):
    corpus = [[' '.join(map(str, (list(e)))).replace(' ', ':') for e in ele] for ele in corpus]

    f = open('./data/75.scale', 'w')
    n = min(len(corpus), len(feature.target))
    for i in range(n):
        f.write(str(feature.target[i]) + ' ' + ' '.join([e for e in corpus[i]]) + '\n')
    f.close()


def highest_rank(models, limit=10):
    higher = []

    for line in models:
        weight = line.split()
        if re.search('[a-zA-Z]+', weight[0]) is None:
            if len(higher) < limit:
                higher.append(weight)
            elif weight[0] < sorted(higher, key=lambda x: x[0], reverse=True)[-1][0]:
                higher.remove(sorted(higher, key=lambda x: x[0])[-1])
                higher.append(weight)
    return higher


def lowest_rank(models, limit=10):
    lower = []

    for line in models:
        weight = line.split()
        if re.search('[a-zA-Z]+', weight[0]) is None:
            if len(lower) < limit:
                lower.append(weight)
            elif weight[0] < sorted(lower, key=lambda x: x[0], reverse=True)[-1][0]:
                lower.remove(sorted(lower, key=lambda x: x[0])[-1])
                lower.append(weight)
    return lower


if __name__ == '__main__':
    lines = load_txt()
    stems = stem(lines)
    feature = create_feature(lines, stems)
    logreg = modelize(feature)

    if 'chapter8.dict' and 'chapter8.mm' not in os.listdir('/tmp/'):
        dictionary = create_dict(stems)
        create_corpus(dictionary, stems)

    dictionary = gensim.corpora.Dictionary.load('/tmp/chapter8.dict')
    corpus = gensim.corpora.MmCorpus('/tmp/chapter8.mm')

    if '75.scale' not in os.listdir('./data/'):
        create_scale(corpus, feature)

    # 素性数が多い場合、線形カーネル(ただの内積): K(u,v) = uTvを使うと上手くいきやすいので -t 0を使う
    if '75.scale.model' not in os.listdir('./data'):
        cmd1 = 'svm-train -t 0 -h 0 data/75.scale ; mv 75.scale.model data/'
        subprocess.call(cmd1, shell=True)

        cmd2 = 'svm-predict data/75.scale data/75.scale.model data/accuracy.txt > data/accuracy.txt'
        subprocess.call(cmd2, shell=True)

    with open('data/75.scale.model', encoding='utf-8') as f:
        models = f.readlines()

    higher = highest_rank(models)
    lower = lowest_rank(models)

    print('Highest feature are')
    for w in sorted(higher, key=lambda x: x[0]):
        weight = w.pop(0)
        print(weight, '\t', ' '.join(w), '\n')

    print('Lowest feature are')
    for w in sorted(lower, key=lambda x: x[0]):
        weight = w.pop(0)
        print(weight, '\t', ' '.join(w), '\n')
