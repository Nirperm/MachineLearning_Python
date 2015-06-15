class FeatureReader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.feature_dict = {}

    def read_feature(self):
        with open(self.file_name, encoding='utf-8') as f:
            for line in f:
                line = line.replace('\n', '')
                split_label = line.split('\t')
                split_word = split_label[1].split(' ')
                sentence = ' '.join(split_word)
                self.feature_dict.update({split_label[0]: sentence})
