class Reader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.word_list = []
        self.total_word_size = 0

    def read_file(self):
        with open(self.file_name, encoding='utf-8') as f:
            for line in f:
                rline = line.replace('\n', '')
                split_word = rline.split(' ')
                split_word.append('</s>')
                self.word_list.append(split_word)
                self.total_word_size += len(split_word)
