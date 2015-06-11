class Reader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.word_list = []
        self.total_word = 0

    def read_file(self):
        with open(self.file_name, encoding='utf-8') as f:
            for line in f:
                line = line.replace('\n', '')
                line_list = line.split(' ')
                line_list.append('</s>')
                self.word_list.append(line_list)
                self.total_word += len(line_list)
