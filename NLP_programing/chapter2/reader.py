class Reader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.word_list = []

    def read_file(self):
        with open(self.file_name, encoding='utf-8') as f:
            for line in f:
                line = line.replace('\n', '')
                split_line = line.split(' ')
                split_line.append('</s>')
                split_line.insert(0, '<s>')
                self.word_list.append(split_line)
