# MachineLearning_Python

## Description
* Practice Marchine Learning to write lines of python code.
* Python vesrion is 3.4.2.

##  Requirements
* `pip install -r requirements.txt`
* OS package manager install Graphviz, Redis, MongoDB
* Need additional install of Certifi, MeCab and CaboCha, pydot.  
* graphviz is is particular kind of install. https://github.com/pygraphviz/pygraphviz/issues/16 and http://qiita.com/shimo_t/items/b761973805f2cf0b2967 
* pydot is particular kind of install. Run `git clone https://github.com/nlhepler/pydot.git & cd pydot & pip install -e .`
* In case of MacOS, `brew install libsvm`  
 * `pip install -e git+https://github.com/Salinger/libsvm-python.git#egg=libsvm-python`
* In case of Other platform get [zip](http://www.csie.ntu.edu.tw/~cjlin/cgi-bin/libsvm.cgi?+http://www.csie.ntu.edu.tw/~cjlin/libsvm+zip) or [tar.gz] (http://www.csie.ntu.edu.tw/~cjlin/cgi-bin/libsvm.cgi?+http://www.csie.ntu.edu.tw/~cjlin/libsvm+tar.gz)  
 * At the command prompt `cd /libsvm ; make`,  `cd /python　; make or gmake`

## Test
`python -m unittest tests/test~*.py`

## Refer
* Forked from [SnowMasaya/MachineLearning_Python](https://github.com/SnowMasaya/MachineLearning_Python).
* NLP100_knock refers to the [言語処理100本ノック 2015](http://www.cl.ecei.tohoku.ac.jp/nlp100/).
* NLP_progrmaming refers to the [Graham Neubig](http://www.phontron.com/teaching.php?lang=ja).

## TODO
[my_task](https://github.com/Nirperm/MachineLearning_Python/issues/1)
