from math import log


class EvaluateModel:

    LAMBDA_P1 = 0.95
    LAMBDA_P2 = 0.95
    LAMBDA_UNK1 = 1 - LAMBDA_P1
    LAMBDA_UNK2 = 1 - LAMBDA_P2
    V = 1000000  # Volume
    H = 0  # Entropy

    def __init__(self, file_name, word_prob, lambda_word_dict):
        self.file_name = file_name
        self.word_prob = word_prob
        self.total_word_count = 0
        self.lambda_word_p = lambda_word_dict

    def evaluate(self):
        with open(self.file_name, encoding='utf-8') as f:
            for line in f:
                line = line.replace('\n', '')
                word_list = line.split(' ')
                word_list.append('</s>')
                word_list.insert(0, '<s>')
                count = 1
                while len(word_list) > count:
                    self.total_word_count = self.total_word_count + 1
                    P1 = 1.0 * self.LAMBDA_UNK1 / self.V
                    if word_list[count] in self.word_prob:
                        P1 = P1 + (1 - self.lambda_word_p[word_list[count - 1]]) * self.word_prob[word_list[count]]
                    P2 = P1 * self.lambda_word_p[word_list[count - 1]] / self.V
                    bi_word = word_list[count - 1] + ' ' + word_list[count]
                    if word_list[count] in self.word_prob:
                        P2 = P2 + self.lambda_word_p[word_list[count - 1]] * self.word_prob[bi_word]
                    self.H = self.H - 1 * log(P2, 2)
                    count = count + 1
