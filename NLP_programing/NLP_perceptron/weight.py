class Weight:

    def __init__(self, weight, phi, y):
        self.weight = weight
        self.phi = phi  # Φ ファイ
        self.y = y  # label for weight

    def update(self):
        for name, value in self.phi.items():
            self.weight[name] = float(self.weight[name]) + float(value) * int(self.y)
        return self.weight
