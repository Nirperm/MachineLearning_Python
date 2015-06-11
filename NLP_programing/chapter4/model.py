class Model:

    def __init__(self, file_name):
        self.file_name = file_name
        self.word_dict = {}

    def read_file(self):
        with open(self.file_name, encoding='utf-8') as f:
            for line in f:
                word = line.split(' ')
                prob = float(word[1])
                self.word_dict.update({word[0]: prob})
