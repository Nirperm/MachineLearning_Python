class TrainUnigram:

    def __init__(self, word, total_word_count):
        self.word = word
        self.word_dict = {}
        self.total_word_count = total_word_count

    def train(self):
        for word_line in self.word:
            for word_unit in word_line:
                if word_unit in self.word_dict:
                    value = self.word_dict[word_unit]
                    self.word_dict.update({word_unit: value + 1})
                else:
                    self.word_dict[word_unit] = 1
        for k, v in self.word_dict.items():
            prob = 1.0 * v / self.total_word_count
            self.word_dict.update({k: prob})
