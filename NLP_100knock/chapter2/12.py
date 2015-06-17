"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcurlコマンドを用いよ．
"""

import subprocess

input_file = 'data/hightemp.txt'

output_file1 = 'data/col1.txt'
output_file2 = 'data/col2.txt'

col1 = open(output_file1, 'w', encoding='utf-8')
col2 = open(output_file2, 'w', encoding='utf-8')

with open(input_file, encoding='utf-8') as f:
    for line in f:
        split_line = line.split()
        col1.write(split_line[0] + '\n')
        col2.write(split_line[1] + '\n')

col1.close()
col2.close()

cmd1 = 'curl -O {0}'.format("https://github.com/Nirperm/MachineLearning_Python/tree/master/NLP_100knock/chapter2/data/col1.txt")
cmd2 = 'curl -O {0}'.format('https://github.com/Nirperm/MachineLearning_Python/tree/master/NLP_100knock/chapter2/data/col2.txt')

subprocess.call(cmd1, shell=True)
subprocess.call(cmd2, shell=True)
