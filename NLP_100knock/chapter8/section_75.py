"""
75. 素性の重み
73で学習したロジスティック回帰モデルの中で，
重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．
"""


def main():
    lower = list()
    higher = list()
    lim = 10

    for line in open('data/73_model.txt'):
        if line.startswith('@'):
            continue
        weight = line.strip().split()
        weight[0] = float(weight[0])

        if len(lower) < lim:
            lower.append(weight)
        elif weight[0] < sorted(lower, key=lambda x: x[0])[-1][0]:
            lower.remove(sorted(lower, key=lambda x: x[0])[-1])
            lower.append(weight)

        if len(higher) < lim:
            higher.append(weight)
        elif weight[0] > sorted(higher, key=lambda x: x[0])[0][0]:
            higher.remove(sorted(higher, key=lambda x: x[0])[0])
            higher.append(weight)


    print('High weight lank')
    for w in sorted(higher, key=lambda x: -x[0]):
        print(w[0], w[1])


    print('Low weight lank')
    for w in sorted(lower, key=lambda x: x[0]):
        print(w[0], w[1])

if __name__ == '__main__':
    main()
