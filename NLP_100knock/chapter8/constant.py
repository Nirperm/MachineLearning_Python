import nltk
STOPWORDS = nltk.corpus.stopwords.words('english')
STOPWORDS.append('"')
STOPWORDS.append('.')
STOPWORDS.append(',')
STOPWORDS.append('')
STOPWORDS.append('(')
STOPWORDS.append(')')
STOPWORDS.append('+1')
STOPWORDS.append('--')
STOPWORDS.append('-1')
STOPWORDS.append(':')
STOPWORDS.append('&')
STOPWORDS.append('!')
STOPWORDS.append('?')
STOPWORDS.append(';')
STOPWORDS.append('%')
STOPWORDS.append('*')
STOPWORDS.append('everyone\'s')
STOPWORDS.append('one\'s')
STOPWORDS.append('it\'s')
STOPWORDS.append('who\'s')
STOPWORDS.append('whose')
STOPWORDS.append('i\'m')
STOPWORDS.append('i\'ve')
STOPWORDS.append('you\'re')
STOPWORDS.append('you\'d')
STOPWORDS.append('you\'ll')
STOPWORDS.append('you\'ve')
STOPWORDS.append('he\'s')
STOPWORDS.append('we\'re')
STOPWORDS.append('we\'ve')
STOPWORDS.append('us')
STOPWORDS.append('done')
STOPWORDS.append('haven\'t')
STOPWORDS.append('hasn\'t')
STOPWORDS.append('hadn\'t')
STOPWORDS.append('what\'s')
STOPWORDS.append('they\'re')
STOPWORDS.append('that\'s')
STOPWORDS.append('there\'s')
STOPWORDS.append('isn\'t')
STOPWORDS.append('weren\'t')
STOPWORDS.append('don\'t')
STOPWORDS.append('doesn\'t')
STOPWORDS.append('can\'t')
STOPWORDS.append('could')
STOPWORDS.append('would')
STOPWORDS.append('wouldn\'t')
STOPWORDS.append('won\'t')
STOPWORDS.append('would\'ve')
STOPWORDS.append('may')
STOPWORDS.append('might')
