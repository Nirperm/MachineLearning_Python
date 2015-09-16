"""
82. 文脈の抽出
81で作成したコーパス中に出現するすべての単語tに関して，単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．
ただし，文脈語の定義は次の通りとする．

ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．
"""

import random


def back_and_forth_ngram():
    for line in open('data/81_result.txt'):
        spl = line.strip().split()
        for i in range(len(spl)):
            n = random.randint(1, 5)
            all_range_indices = [ii + 1 for ii in range(n)] + [-(ii + 1) for ii in range(n)]
            context_indices = [ii + i for ii in all_range_indices if ii + i >= 0 and ii + i < len(spl)]
            print(' '.join([spl[i]]) + '\t' + '\t'.join([spl[ii] for ii in context_indices]))


if __name__ == '__main__':
    back_and_forth_ngram()
