class Reader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.word_list = []

    def read_file(self):
        with open(self.file_name, encoding='utf-8') as f:
            for line in f:
                rline = line.replace('\n', '')
                split_list = rline.split(' ')
                split_list.append('</s>')
                split_list.insert(0, '<s>')
                self.word_list.append(split_list)
