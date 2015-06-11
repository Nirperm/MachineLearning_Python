from ngram import Ngram


class TrainNgram:

    def __init__(self, word, ngram_size):
        self.word = word
        self.ngram_size = ngram_size
        self.word_dict = {}
        self.context_dict = {}
        self.lambda_word_dict = {}

    def train(self):
        bi_diff_word_dict = {}
        u_count_dict_key = {}
        count_dict_key = {}
        for word_line in self.word:
            count = 1
            while len(word_line) > count:
                ngram_count = 2
                word_dict = Ngram(self.word_dict, word_line[count])
                self.word_dict = word_dict.count_dict_key()

                count_dict_key = Ngram(count_dict_key, word_line[count - 1])
                count_dict_key = count_dict_key.count_dict_key()

                context_dict = Ngram(self.context_dict, '')
                self.context_dict = context_dict.count_dict_key()

                while self.ngram_size >= ngram_count:
                    n_word = []
                    for counter in range(0, ngram_count):
                        unit_number = count - 1 + counter
                        if len(word_line) <= unit_number:
                            break
                        n_word.append(word_line[unit_number])
                    join_nword = ' '.join(n_word)
                    word_dict = Ngram(self.word_dict, join_nword)
                    self.word_dict = word_dict.count_dict_key()
                    context_dict = Ngram(self.context_dict, join_nword)
                    self.context_dict = context_dict.count_dict_key()
                    ngram_count = ngram_count + 1
                bi_word = word_line[count - 1] + ' ' + word_line[count]
                bi_diff_word_dict.update({bi_word: word_line[count - 1]})
                context_dict = Ngram(self.context_dict, word_line[count - 1])
                self.context_dict = context_dict.count_dict_key()

                count = count + 1
        """ Bell Smoothing """
        for k, v in bi_diff_word_dict.items():
            words = k.split(' ')
            if v in u_count_dict_key:
                bi_value = u_count_dict_key[v]
                u_count_dict_key.update({v: bi_value + 1})
            else:
                u_count_dict_key[v] = 1

        for k in count_dict_key.keys():
            lambda_w = 1 - (1.0 * u_count_dict_key[k] / (u_count_dict_key[k] + count_dict_key[k]))
            self.lambda_word_dict.update({k: lambda_w})

        print({k: v for k, v in self.word_dict.items()})
        for ngram, count in self.word_dict.items():
            words = ngram.split(' ')
            words.pop()
            if len(words) < 2:
                context = ''.join(words)
            else:
                context = ' '.join(words)
            prob = 1.0 * self.word_dict[ngram] / self.context_dict[context]
            self.word_dict.update({ngram: prob})
