"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""

import subprocess
import sys


if len(sys.argv) is 2:
    input_file = 'data/hightemp.txt'
    count_size = sys.argv[1]
    with open(input_file, encoding='utf-8') as f:
        print(''.join(f.readlines()[:int(count_size)]))

    cmd = 'head -n {0} {1}'.format(int(count_size), input_file)
    subprocess.call(cmd, shell=True)

else:
    print('give params with natural number')
