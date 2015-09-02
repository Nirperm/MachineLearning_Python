"""
77. 正解率の計測
76の出力を受け取り，
予測の正解率，正例に関する適合率，再現率，F1スコアを求めるプログラムを作成せよ．
"""

# refer to http://d.hatena.ne.jp/sleepy_yoshi/20110410/p1
# FIXME: Libsvm output is wrong, fix section_75.py

if __name__ == '__main__':
    with open('data/76.txt', encoding='utf-8') as f:
        lines = f.readlines()

    tp = .0  # True Positive
    fp = .0  # False Positive
    fn = .0  # True Negative
    tn = .0  # False Negative

    for line in lines:
        ans, pred, prob = line.strip().split()
        if ans == pred:
            if ans == "+1":
                tp += 1
            else:
                tn += 1
        else:
            if ans == "+1":
                fn += 1
            else:
                fp += 1

    accuracy = (tp + tn) / float(tp + tn + fn + fp)
    precision = tp / float(tp + fp)
    recall = tp / float(tp + fn)
    f1 = 2 * precision * recall / (precision + recall)
    print("accuracy", accuracy)
    print("precision", precision)
    print("recall", recall)
    print("f1", f1)
