"""
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

import subprocess

input_file = 'data/hightemp.txt'

cmd = 'wc -l {0}'.format(input_file)
subprocess.call(cmd, shell=True)
