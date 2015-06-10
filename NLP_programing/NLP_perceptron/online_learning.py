from feature_creator import FeatureCreator
from train_one_prediction import TrainOnePrediction
from weight import Weight


class OnlineLearning:

    def __init__(self, feature, data, flabel):
        self.feature = feature
        self.data = data
        self.phi = {}  # Φファイ
        self.label = 0
        self.flabel = flabel
        self.weight = {}
        self.iteration = 1000

    def online_learning(self):
        count = 0

        """ initinalize """
        for value in self.feature.values():
            split_word = value.split(' ')
            [self.weight.update({self.flabel + word: 0}) for word in split_word]
        cfeature = FeatureCreator()

        """ update weight """
        while self.iteration >= count:
            count = count + 1
            for key, value in self.feature.items():
                self.phi = cfeature.create(value, self.data, self.flabel)
                self.label = TrainOnePrediction(self.weight, self.phi)
                if self.label is not key:
                    update_weight = Weight(self.weight, self.phi, key)
                    self.weight = update_weight.update()
