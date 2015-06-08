class Writer:

    def __init__(self, file_name, unigram_dict):
        self.file_name = file_name
        self.unigram_dict = unigram_dict

    def write_file(self):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            for k, v in self.unigram_dict.items():
                word = k.replace('\n', '')
                f.write(word + ' ' + str(v))
                f.write('\n')
