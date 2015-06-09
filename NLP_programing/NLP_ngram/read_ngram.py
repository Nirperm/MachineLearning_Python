class ReadNgram:

    def __init__(self, file_name):
        self.file_name = file_name
        self.word_dict = {}

    def read_model(self):
        with open(self.file_name, encoding='utf-8') as f:
            for line in f:
                word_list = line.split(' ')
                prob = float(word_list[len(word_list) - 1])
                word_list.pop()
                word = str(' '.join(word_list))
                self.word_dict.update({word: prob})
