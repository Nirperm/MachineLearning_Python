class Writer:

    def __init__(self, file_name, unigram_model):
        self.file_name = file_name
        self.unigram_model = unigram_model

    def write_file(self):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            for key, value in self.unigram_model.items():
                word = key.replace('\n', '')
                f.write(word + ' ' + str(value))
                f.write('\n')
