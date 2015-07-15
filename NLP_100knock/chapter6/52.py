"""
52. ステミング
51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ．
Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．
"""


from nltk.stem import PorterStemmer, WordNetLemmatizer
from section_50 import divide_content
from section_51 import divide_word


def stemmer(word_list):
    stemmer = PorterStemmer()
    lemmatiser = WordNetLemmatizer()

    for word in word_list:
        print('Lemmatise:{0} \t  Stem:{1}'.format(lemmatiser.lemmatize(word.strip(), pos='v'), stemmer.stem(word.strip())))


if __name__ == '__main__':
    sentence_list = divide_content()
    word_list = divide_word(sentence_list)
    stemmer(word_list)
