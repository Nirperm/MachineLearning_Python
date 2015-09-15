"""
91. アナロジーデータの準備
単語アナロジーの評価データをダウンロードせよ．このデータ中で": "で始まる行はセクション名を表す．
例えば，": capital-common-countries"という行は，"capital-common-countries"というセクションの開始を表している．
ダウンロードした評価データの中で，"family"というセクションに含まれる評価事例を抜き出してファイルに保存せよ．
"""


with open('data/questions-words.txt') as f:
    lines = f.readlines()

f = open('data/family.txt', 'w')

flag = False
for line in lines:
    if line.startswith(':'):
        if flag:
            break
        flag = False

    if line.startswith(': family'):
        flag = True

    if flag:
        f.write(line)

f.close()
