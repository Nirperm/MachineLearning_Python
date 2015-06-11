class FeatureCreator:
    def __init__(self):
        self.phi = {}  # Φファイ

    def create(self, feature, data, flabel):
        split_word = feature.split(' ')
        for word in split_word:
            feature = flabel + word
            self.phi.update({feature: data[word]})
        return self.phi
