from bigram import Bigram


class TrainBigram:

    def __init__(self, word):
        self.word = word
        self.word_dict = {}
        self.context_count_dict = {}
        self.lambda_word_dict = {}

    def train(self):
        bi_diff_word_dict = {}
        u_count_dict = {}
        count_word_dict = {}
        for word_line in self.word:
            count = 1
            while len(word_line) > count:
                word_dict = Bigram(self.word_dict, word_line[count])
                self.word_dict = word_dict.dict_bigram()

                count_word_dict = Bigram(count_word_dict, word_line[count - 1])
                count_word_dict = count_word_dict.dict_bigram()

                context_count_dict = Bigram(self.context_count_dict, '')
                self.context_count_dict = context_count_dict.dict_bigram()

                bi_word = word_line[count - 1] + ' ' + word_line[count]
                word_dict = Bigram(self.word_dict, bi_word)
                self.word_dict = word_dict.dict_bigram()
                bi_diff_word_dict.update({bi_word: word_line[count - 1]})

                context_count_dict = Bigram(self.context_count_dict, word_line[count - 1])
                self.context_count_dict = context_count_dict.dict_bigram()

                count = count + 1

        # Witten Bell Smoothing
        for k, v in bi_diff_word_dict.items():
            # split_word = k.split(' ')
            if v in u_count_dict:
                bi_value = u_count_dict[v]
                u_count_dict.update({v: bi_value + 1})
            else:
                u_count_dict[v] = 1

        for k in count_word_dict.keys():
            lambda_w = 1 - (1.0 * u_count_dict[k] / (u_count_dict[k] + count_word_dict[k]))
            self.lambda_word_dict.update({k: lambda_w})
        #
        for ngram, count in self.word_dict.items():
            n_split_word = ngram.split(' ')
            n_split_word.pop()
            context = ''.join(n_split_word)
            prob = 1.0 * self.word_dict[ngram] / self.context_count_dict[context]
            self.word_dict.update({ngram: prob})
