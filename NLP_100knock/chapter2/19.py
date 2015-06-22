"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．
"""


import subprocess


input_file = 'data/hightemp.txt'
words = {}
with open(input_file, encoding='utf-8') as f:
    lines = f.readlines()
    divide_lines = [''.join(lines[i:i + 1]).split('\t') for i in range(0, len(lines), 1)]

    for lines in divide_lines:
        words[lines[0]] = words.get(lines[0], 0) + 1

    word_dic = [(v, k) for k, v in words.items()]
    word_dic.sort()
    word_dic.reverse()
    for count, word in word_dic:
        print(count, word)

print('\n')
cmd = 'cut -f 1 {0} | sort | uniq -c | sort -r'.format(input_file)
subprocess.call(cmd, shell=True)
