class Reader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.word_list = []

    def file_Read(self):
        with open(self.file_name, encoding='utf-8') as f:
            for line in f:
                rline = line.replace('\n', '')
                split_word = rline.split(' ')
                split_word.append('</s>')
                split_word.insert(0, '<s>')
                self.word_list.append(split_word)
