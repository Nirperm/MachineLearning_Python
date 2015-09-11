# MachineLearning_Python

## Description
* Practice Marchine Learning to write lines of python code
* Python vesrion is 3.4.2

##  Requirements
* `pip install -r requirements.txt`
* OS package manager need to install Graphviz, Redis, MongoDB, libvsm
* Need additional install of Certifi, MeCab, CaboCha
* Install Graphvizm  refer to http://pod.hatenablog.com/entry/2015/03/07/163911 and http://qiita.com/shimo_t/items/b761973805f2cf0b2967 
* Install Pydot, Run `git clone https://github.com/nlhepler/pydot.git & cd pydot & pip install -e .`
* Install libsvm
 * `brew install libsvm` in case of MacOS, `pip install -e git+https://github.com/Salinger/libsvm-python.git#egg=libsvm-python`
 *  Get [zip](http://www.csie.ntu.edu.tw/~cjlin/cgi-bin/libsvm.cgi?+http://www.csie.ntu.edu.tw/~cjlin/libsvm+zip) or [tar.gz] (http://www.csie.ntu.edu.tw/~cjlin/cgi-bin/libsvm.cgi?+http://www.csie.ntu.edu.tw/~cjlin/libsvm+tar.gz) , at the command prompt `cd /libsvm ; make`,  `cd /python　; make or gmake` in other platform 

* Install word2vec
  * Refer to http://aipacommander.hatenablog.jp/entry/2014/09/11/220747 in case of mac
  * Refer to http://qiita.com/okappy/items/e16639178ba85edfee72 in case of Other platform


## Test
`python -m unittest tests/test~*.py`

## Refer
* Forked from [SnowMasaya/MachineLearning_Python](https://github.com/SnowMasaya/MachineLearning_Python)
* NLP100_knock comes from [言語処理100本ノック 2015](http://www.cl.ecei.tohoku.ac.jp/nlp100/)
* NLP_progrmaming comes from [Graham Neubig](http://www.phontron.com/teaching.php?lang=ja)

## TODO
[my_task](https://github.com/Nirperm/MachineLearning_Python/issues/1)
