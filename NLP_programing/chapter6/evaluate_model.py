from math import log


class EvaluateModel:

    LAMBDA_PARM1 = 0.95
    LAMBDA_PARM2 = 0.95
    LAMBDA_UNK1 = 1 - LAMBDA_PARM1
    LAMBDA_UNK2 = 1 - LAMBDA_PARM2
    V = 1000000  # Volume
    H = 0  # Entropy

    def __init__(self, file_name, word_prob, lambda_word_dict):
        self.file_name = file_name
        self.word_prob = word_prob
        self.total_word_count = 0
        self.lambda_word_param = lambda_word_dict

    def evaluate_model(self):
        with open(self.file_name, encoding='utf-8') as f:
            for line in f:
                line = line.replace('\n', '')
                split_line = line.split(' ')
                split_line.append('</s>')
                split_line.insert(0, '<s>')
                count = 1
                while len(split_line) > count:
                    self.total_word_count += 1
                    P1 = 1.0 * self.LAMBDA_UNK1 / self.V
                    if split_line[count] in self.word_prob:
                        P2 = P1 * self.lambda_word_param[split_line[count - 1]] / self.V
                        bi_word = split_line[count - 1] + ' ' + split_line[count]
                    if split_line[count] in self.word_prob:
                        P2 = P2 + self.lambda_word_param[split_line[count - 1]] * self.word_prob[bi_word]
                        self.H = self.H - 1 * log(P2, 2)
                        count = count + 1
