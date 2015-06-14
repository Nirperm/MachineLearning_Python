class Model:

    def __init__(self, file_name):
        self.file_name = file_name
        self.word_dict = {}

    def read_model(self):
        with open(self.file_name, 'r', encoding='utf-8') as f:
            for line in f:
                split_line = line.split(' ')
                prob = float(split_line[1])
                self.word_dict.update({split_line[0]: prob})
