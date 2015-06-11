from math import log


class BackwardViterbi:  # HACK: is this class correct?

    def __init__(self, unigram_model_name, file_name):
        self.file_name = file_name
        self.unigram_model_name = unigram_model_name
        self.unigram = {}
        self.best_edges = []
        self.best_scores = []

    def backward_process(self):
        with open(self.unigram_model_name, encoding='utf-8') as model:
            for line in model:
                rline = line.replace('\n', '')
                split_list = rline.split(' ')
                self.unigram.update({split_list[0]: split_list[1]})
            print({k: v for k, v in self.unigram.items()})

        with open(self.file_name, encoding='utf-8') as f:
            for line in f:
                rline = line.replace('\n', '')
                self.best_edges.insert(0, None)
                self.best_scores.insert(0, 0)
                for word_end in range(1, len(rline) + 1):
                    self.best_scores.insert(word_end, 10 ** 10)
                    for word_begin in range(0, word_end):
                        word = rline[word_begin:word_end]
                        if word in self.unigram or len(word) == 1:
                            prob = self.unigram[word]
                            my_score = self.best_scores[word_begin] - log(float(prob))
                        if my_score < self.best_scores[word_end]:
                            self.best_scores.insert(word_end, my_score)
                            self.best_edges.insert(word_end, (word_begin, word_end))

        word_list = []
        next_edge = self.best_edges[len(self.best_edges) - 1]
        while next_edge is not None:
            rline = line[next_edge[0]:next_edge[1]]
            word_list.append(rline)
            next_edge = self.best_edges[next_edge[0]]
        word_list.reverse()
        print(' '.join(word_list))
