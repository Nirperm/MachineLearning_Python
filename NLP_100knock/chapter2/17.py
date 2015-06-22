"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．
確認にはsort, uniqコマンドを用いよ．
"""


import subprocess

input_file = 'data/hightemp.txt'
with open(input_file, encoding='utf-8') as f:
    lines = f.readlines()
    divide_lines = [''.join(lines[i:i + 1]).split('\t') for i in range(0, len(lines), 1)]
    uniq_list = []
    for lines in divide_lines:
        if lines[0] not in uniq_list:
            uniq_list.append(lines[0])

    uniq_str = ','.join(uniq_list)
    prefecture = uniq_str.replace(',', '\n')
    print(prefecture, '\n')

cmd = 'sort {0}| uniq'.format(input_file)
subprocess.call(cmd, shell=True)
