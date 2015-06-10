class TrainOnePrediction:

    def __init__(self, weight, phi):
        self.weight = weight
        self.phi = phi
        self.score = 0

    def predict(self):
        for name, value in self.phi.iteritems():
            if self.weight[name]:
                self.score = self.score + value * self.weight[name]
        if self.score >= 0:
            return 1
        else:
            return -1
