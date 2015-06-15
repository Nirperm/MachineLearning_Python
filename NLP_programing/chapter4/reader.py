class Reader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.word_list = []
        self.total_word_count = 0

    def read_file(self):
        with open(self.file_name, encoding='utf-8') as f:
            for line in f:
                line = line.replace('\n', '')
                split_line = line.split(' ')
                split_line.append('</s>')
                self.word_list.append(split_line)
                self.total_word_count = self.total_word_count + len(split_line)
