"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""

import subprocess

input_file = 'data/hightemp.txt'
with open(input_file, encoding='utf-8') as f:
    lines = f.readlines()
    group_by = 1
    print('\t'.join(lines))

cmd = 'sort -k 3r,3 {0}'.format(input_file)
subprocess.call(cmd, shell=True)
