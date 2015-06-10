class OnePrediction:

    def __init__(self, file_name, weight, phi, flabel):
        self.file_name = file_name
        self.weight = weight
        self.phi = phi
        self.flabel = flabel
        self.score = 0

    def predict(self):
        with open(self.file_name, encoding='utf-8') as f:
            for line in f:
                rline = line.replace('\n', '')
                split_word = rline.split(' ')
                score = 0
                for word in split_word:
                    name = self.flabel + word
                    if self.weight[name]:
                        score = score + self.phi[name] * self.weight[name]
                if score >= 0:
                    print(str(1) + '\t' + line)
                else:
                    print(str(-1) + '\t' + line)
