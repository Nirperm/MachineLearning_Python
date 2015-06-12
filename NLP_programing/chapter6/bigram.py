class Bigram:

    def __init__(self, word_dict, word):
        self.word_dict = word_dict
        self.word = word

    def dict_bigram(self):
        if self.word in self.word_dict:
            value = self.word_dict[self.word]
            self.word_dict.update({self.word: value + 1})
        else:
            self.word_dict[self.word] = 1
        return self.word_dict
