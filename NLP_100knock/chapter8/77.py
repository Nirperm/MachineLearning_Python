"""
77. 正解率の計測
76の出力を受け取り，
予測の正解率，正例に関する適合率，再現率，F1スコアを求めるプログラムを作成せよ．
"""

# refer to http://d.hatena.ne.jp/sleepy_yoshi/20110410/p1
# FIXME: Libsvm output is wrong, fix section_75.py

if __name__ == '__main__':
    predict_file = open('data/76.txt', 'r')


    all_count = 0
    concord_count = 0
    correct_count = 0
    correct_match_count = 0
    pre = 0
    for line in predict_file:
        all_count += 1
        print(line)
        correct, predict, prob = line.split()
        if correct == predict:
            concord_count += 1
        if correct == '-1':
            correct_count += 1
            if correct == predict:
                correct_match_count += 1
        if predict == '+1':
            pre += 1

    print('rate of concordance:', float(concord_count) / float(all_count))
    print(float(pre))
    pre = correct_match_count / float(pre)
    rec = correct_match_count / float(correct_count)
    print('Precision:', pre)
    print('Recall:', rec)
    print('F-measure:', 2 * rec * pre / (rec + pre))
