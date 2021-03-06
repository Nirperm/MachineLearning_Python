from math import log


class EvaluateModel:

    LAMBDA_P = 0.95
    LAMBDA_UNK = 1 - LAMBDA_P
    V = 1000000  # Volume
    H = 0  # Entropy

    def __init__(self, file_name, word_prob):
        self.file_name = file_name
        self.word_prob = word_prob
        self.total_word_count = 0
        self.unknown_word_count = 0

    def evaluate(self):
        with open(self.file_name, encoding='utf-8') as f:
            for line in f:
                line = line.replace('\n', '')
                split_line = line.split(' ')
                split_line.append('</s>')
                for word in split_line:
                    self.total_word_count = self.total_word_count + 1
                    P = 1.0 * self.LAMBDA_UNK / self.V
                    if word in self.word_prob:
                        P = P + self.LAMBDA_P * self.word_prob[word]
                    else:
                        self.unknown_word_count = self.unknown_word_count + 1
                    self.H = self.H - 1 * log(P, 2)
