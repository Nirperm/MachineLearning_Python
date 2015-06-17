"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，
元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
"""

import subprocess

input_file1 = 'data/col1.txt'
input_file2 = 'data/col2.txt'

cmd = 'paste -d "\t" {0} {1}  > data/merge.txt'.format(input_file1, input_file2)
result = subprocess.call(cmd, shell=True)
