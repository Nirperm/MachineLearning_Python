"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，
入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ．
"""

import subprocess
import sys


if len(sys.argv) is 2:
    input_file = 'data/hightemp.txt'
    count_size = sys.argv[1]
    with open(input_file, encoding='utf-8') as f:
        lines = f.readlines()
        divide_lines = [lines[i:i + int(count_size)] for i in range(0, len(lines), int(count_size))]
        for divide_line in divide_lines:
            print(''.join(divide_line))

    cmd = 'split -l {0} {1} data/split.txt'.format(int(count_size), input_file)
    subprocess.call(cmd, shell=True)

else:
    print('give params with natural number')
