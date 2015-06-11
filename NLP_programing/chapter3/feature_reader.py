class FeatureReader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.feature_dict = {}

    def read_feature(self):
        with open(self.file_name, encoding='utf-8') as f:
            for line in f:
                rline = line.replace('\n', '')
                label_list = rline.split('\t')
                split_word = label_list[1].split(' ')
                sentence = ' '.join(split_word)
                self.feature_dict.update({label_list[0]: sentence})
