"""
70. データの入手・整形
文に関する極性分析の正解データを用い，
以下の要領で正解データ（sentiment.txt）を作成せよ．

rt-polarity.posの各行の先頭に"+1 "という文字列を追加する
（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）

rt-polarity.negの各行の先頭に"-1 "という文字列を追加する
（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）

上述1と2の内容を結合（concatenate）し，行をランダムに並び替える

sentiment.txtを作成したら，
正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．
"""
import random

all_content_list = []
with open('data/rt-polaritydata/rt-polarity.pos') as f1:
    for line in f1:
        all_content_list.append('+1' + '\t' + line)

with open('data/rt-polaritydata/rt-polarity.neg') as f2:
    for line in f2:
        all_content_list.append('-1' + '\t' + line)


random.shuffle(all_content_list)
f = open('data/sentiment.txt', 'w')
for line in all_content_list:
    f.write(line)
f.close()

pos_counter = 0
neg_counter = 0
with open('data/sentiment.txt', encoding='utf-8') as f:
    for line in f:
        content_list = line.split()
        if content_list[0] == '+1':
            pos_counter += 1
        if content_list[0] == '-1':
            neg_counter += 1

print('+1 size is ' + str(pos_counter))
print('-1 size is ' + str(neg_counter))
