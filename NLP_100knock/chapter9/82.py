"""
82. 文脈の抽出
81で作成したコーパス中に出現するすべての単語tに関して，単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．
ただし，文脈語の定義は次の通りとする．

ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．
"""

import random


def back_and_forth_ngram():
    with open('data/81_result.txt', encoding='utf-8') as f:
        texts = f.read()

    texts = [word.split() for word in texts]
    for word in texts:
        n = random.randint(1, 5)
        # print( set(texts[:texts.index(word) + n]) -  set(texts[text.index(word) + n:]) )
    """
    for i in range(len(token)):
        n = random.randint(1, 5)
        print(token[i: n])
    """
if __name__ == '__main__':
    back_and_forth_ngram()
