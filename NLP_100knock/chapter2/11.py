"""
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．
確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""

import subprocess

input_file = 'data/hightemp.txt'

cmd = 'sed -e s/"\t"/" "/g {0}'.format(input_file)
subprocess.call(cmd, shell=True)
