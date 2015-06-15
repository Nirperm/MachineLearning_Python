class ModelReader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.word_dict = {}

    def read_model(self):
        with open(self.file_name, encoding='utf-8') as f:
            for line in f:
                split_line = line.split(' ')
                prob = float(split_line[len(split_line) - 1])
                split_line.pop()
                word = str(' '.join(split_line))
                self.word_dict.update({word: prob})
