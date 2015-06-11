class Wirter:

    def __init__(self, file_name, unigram_model):
        self.file_name = file_name
        self.unigram_model = unigram_model

    def file_write(self):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            for k, v in self.unigram_model.items():
                word = k.replace('\n', '')
                f.write(word + ' ' + str(v))
                f.write('\n')
