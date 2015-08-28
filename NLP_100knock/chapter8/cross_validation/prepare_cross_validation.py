"""
refer to
http://yut.hatenablog.com/entry/20120829/1346197290
http://hy-adversaria.blogspot.jp/2011/04/pythonlibsvm.html
"""

import subprocess

cmd1 = 'perl -MList::Util=shuffle -e "print shuffle(<>)" < ../data/75.scale | split -l 3500'
subprocess.call(cmd1,  shell=True)

cmd2 = 'cat xaa xab > 1.train.txt ; cat xaa xac > 2.train.txt ;  cat xab xac > 3.train.txt ; cat xac xad > 4.train.txt'
subprocess.call(cmd2,  shell=True)

cmd3 = 'mv xac 1.predict.txt ; mv xab 2.predict.txt ; mv xaa 3.predict.txt ; mv xad 4.predict.txt'
subprocess.call(cmd3,  shell=True)

cmd4 = 'svm-train -t 0 -h 1 1.train.txt ; svm-train -t 0 -h 1 2.train.txt ; svm-train -t 0 -h 1 3.train.txt ; svm-train -t 0 -h 1 4.train.txt'
subprocess.call(cmd4,  shell=True)

cmd5 = 'svm-predict 1.predict.txt 1.train.txt.model 1.output.txt > 1.accuracy.txt ; svm-predict 2.predict.txt 2.train.txt.model 2.output.txt > 2.accuracy.txt ; svm-predict 3.predict.txt 3.train.txt.model 3.output.txt > 3.accuracy.txt ; svm-predict 4.predict.txt 4.train.txt.model 4.output.txt > 4.accuracy.txt'
subprocess.call(cmd5,  shell=True)
